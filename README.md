# Overview
Flask API with openapi 3.0.0 to:
- answer question using LLM
- chat with LLM (with history)—history is handled by Sqlite DB (history.db file is created)

# Install
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. create .env file and your `OPENAI_API_KEY=sk-...` key

# Run
1. `source .venv/bin/activate`
2. `python3 app.py`
3. Go to http://localhost:8000/ap/ui to see API documentation
`pytnon3 app.py --help` to see command line parameters