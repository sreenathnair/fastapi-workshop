# fastapi-workshop

## Setup
```
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## Run
```
uvicorn app.app:app --reload
```

## Open API docs

http://localhost:8000/docs


## Run in docker
```
docker compose up
```

## Run tests with coverage with missing lines
```
pip install -r dev-requirements.txt
pytest --cov=app --cov-report term-missing
```

## Pre-commit
```
pip install pre-commit
pre-commit install
```
