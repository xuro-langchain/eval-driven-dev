## Workshop Setup

1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Create a .env file

```bash
cp .env.example .env
# Open .env and fill in the required values
```

3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Load LangSmith assets

```bash
python setup.py
```

## Directory Structure

```
eval-driven-dev/
├── agent.py
├── datasets.py
├── prompts.py
├── requirements.txt
├── setup.py
├── tools.py
├── traces.py
├── utils.py
├── .env.example
├── .gitignore
└── README.md
```

`agent.py` — LangGraph agent that triages emails and calls tools to respond.

`datasets.py` — Defines sample email inputs and reference outputs; loads LangSmith datasets.

`prompts.py` — Prompt definitions and utilities; registers prompts to LangSmith.

`tools.py` — Tool implementations exposed to the agent (email, calendar, Done).

`traces.py` — Runs the agent over dataset examples to generate traces.

`utils.py` — Helper functions for parsing and formatting emails.

`setup.py` — Entry point to load prompts, datasets, and create traces.