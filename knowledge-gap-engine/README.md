# Knowledge Gap Engine

Accuracy engine that analyzes real ticket data to identify missing knowledge base articles and drafts them automatically. Built with Python 3.11, FastAPI, and scikit-learn for NLP clustering.

## Local Development
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Requires PostgreSQL and access to Helply's ticket database.