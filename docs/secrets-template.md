# Secrets Template

Copy this template to a local (untracked) file such as `~/.openclaw/.env` or `.env.agents` and fill in the values.

```
# Web search provider
BRAVE_API_KEY=xxx

# Hugging Face Hub (datasets/models)
HF_TOKEN=xxx

# Semantic Scholar (future)
SEMANTIC_SCHOLAR_API_KEY=xxx

# Kaggle (future)
KAGGLE_USERNAME=...
KAGGLE_KEY=...
```

Notes:
- Never commit the filled-in file.
- After editing, restart the OpenClaw gateway so new env vars are available to tools.
- Hugging Face CLI also reads from `~/.huggingface/token`; keeping the same value in both places simplifies scripting.
