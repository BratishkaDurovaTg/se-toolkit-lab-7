# Bot Development Plan

This bot will be built in small layers so that each step stays testable. In Task 1, the goal is scaffolding: keep command logic in plain Python handler functions, keep configuration loading separate, and keep `bot.py` as the entry point that supports `--test`. That gives one code path for terminal checks now and Telegram integration later.

In Task 2, the bot will start calling the LMS backend. A small API client in `services/` will handle HTTP requests, base URL management, bearer authentication, and friendly error messages. Handlers such as `/health`, `/labs`, and `/scores` will depend on that client instead of calling `httpx` directly.

In Task 3, natural language routing will be added through an LLM client plus tool descriptions for backend actions. The LLM should decide which tool to call; command routing must not be replaced with regex fallbacks. In Task 4, the bot will be containerized, connected to the existing compose stack, configured with environment variables, and deployed on the VM with the same structure used locally.
