# Library Management System: CI/CD with GitHub Actions

Flask REST API with an automated pipeline: **GitHub -> Build -> Automated Testing -> Code Quality Check -> Deployment**.

See [AGILE_PLAN.md](AGILE_PLAN.md) for user stories, sprint plan, DoD and acceptance criteria.

## Run locally
```bash
pip install -r requirements-dev.txt
pytest --cov=app          # tests
flake8 .                  # code quality
python run.py             # start on http://localhost:5000
```

## API
| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /books | Add a book `{"title": "...", "author": "..."}` |
| GET | /books?q=text | Search by title or author |
| POST | /books/{id}/issue | Issue a book |
| POST | /books/{id}/return | Return a book |

Pipeline definition: `.github/workflows/ci-cd.yml`
