#!/usr/bin/env python3
"""Minimal arXiv API helper for OpenClaw agents.

Usage:
  python tools/arxiv_search.py --query "digital twin video africa" --max-results 5

Returns a Markdown-formatted summary of the top matches plus the raw JSON payload
(for agents that want to post-process the data).
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import List

ARXIV_API = "http://export.arxiv.org/api/query"

def fetch_feed(query: str, max_results: int, sort_by: str, sort_order: str) -> str:
    params = {
        "search_query": query,
        "max_results": str(max_results),
        "sortBy": sort_by,
        "sortOrder": sort_order,
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "OpenClaw-Arxiv-Helper"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")

@dataclass
class ArxivEntry:
    title: str
    link: str
    summary: str
    published: str
    authors: List[str]
    categories: List[str]

    def to_markdown(self, idx: int) -> str:
        authors = ", ".join(self.authors) if self.authors else "Unknown"
        cats = ", ".join(self.categories) if self.categories else ""
        summary = textwrap.shorten(" ".join(self.summary.split()), width=400)  # single paragraph
        lines = [
            f"{idx}. **{self.title.strip()}**",
            f"   - Authors: {authors}",
            f"   - Published: {self.published}",
            f"   - Categories: {cats}" if cats else "",
            f"   - Link: {self.link}",
            f"   - Summary: {summary}",
        ]
        return "\n".join([line for line in lines if line])

    def to_dict(self) -> dict:
        return {
            "title": self.title.strip(),
            "link": self.link,
            "summary": self.summary.strip(),
            "published": self.published,
            "authors": self.authors,
            "categories": self.categories,
        }

def parse_feed(xml_text: str) -> List[ArxivEntry]:
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_text)
    entries: List[ArxivEntry] = []
    for e in root.findall("atom:entry", ns):
        title = e.findtext("atom:title", default="", namespaces=ns)
        summary = e.findtext("atom:summary", default="", namespaces=ns)
        published = e.findtext("atom:published", default="", namespaces=ns)
        link = ""
        for link_elem in e.findall("atom:link", ns):
            if link_elem.attrib.get("rel") == "alternate":
                link = link_elem.attrib.get("href", "")
                break
        authors = [a.findtext("atom:name", default="", namespaces=ns) for a in e.findall("atom:author", ns)]
        categories = [c.attrib.get("term", "") for c in e.findall("atom:category", ns)]
        entries.append(ArxivEntry(title=title, link=link, summary=summary, published=published, authors=authors, categories=categories))
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the arXiv API and print structured results.")
    parser.add_argument("--query", required=True, help="Search query (arXiv syntax)")
    parser.add_argument("--max-results", type=int, default=5, help="Number of results to return (max 50 is reasonable)")
    parser.add_argument("--sort-by", choices=["relevance", "lastUpdatedDate", "submittedDate"], default="relevance")
    parser.add_argument("--sort-order", choices=["ascending", "descending"], default="descending")
    parser.add_argument("--json", action="store_true", help="Print JSON only (no Markdown summary)")
    args = parser.parse_args()

    try:
        xml_text = fetch_feed(args.query, args.max_results, args.sort_by, args.sort_order)
        entries = parse_feed(xml_text)
    except Exception as exc:  # noqa: BLE001
        print(f"Error querying arXiv: {exc}", file=sys.stderr)
        sys.exit(1)

    payload = [entry.to_dict() for entry in entries]
    if not args.json:
        print("# arXiv results\n")
        if not entries:
            print("No matches.")
        else:
            for idx, entry in enumerate(entries, start=1):
                print(entry.to_markdown(idx))
                print()
        print("---")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
