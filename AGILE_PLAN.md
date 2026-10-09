# Agile Project Plan: Library Management System

**Course:** Agile Software Development, FA2 (Unit 3 and Unit 4)
**Team:** <Shravani Joshi> and <Dhanshree Ghavas>
**Tech:** Python Flask REST API, pytest, flake8, Docker, GitHub Actions

## 1. Product Vision
A simple web service that lets a librarian add books, search the catalogue, and
issue or return books, so the library always knows which books are available.

## 2. User Stories (Product Backlog)

| ID | User Story | Priority | Story Points |
|----|-----------|----------|--------------|
| US1 | As a **librarian**, I want to **add a new book** with title and author so that it appears in the catalogue. | High | 3 |
| US2 | As a **student**, I want to **search books by title or author** so that I can quickly find what I need. | High | 3 |
| US3 | As a **librarian**, I want to **issue a book** so that I can record that it has been borrowed. | High | 5 |
| US4 | As a **librarian**, I want to **return a book** so that it becomes available to others again. | Medium | 3 |
| US5 | As a **developer**, I want an **automated CI/CD pipeline** so that every change is built, tested, quality-checked and deployed without manual work. | High | 5 |

## 3. Sprint Planning

**Sprint 1** (2 weeks) | **Goal:** Deliver a working, tested and automatically deployed library service.
**Capacity:** 2 members | **Committed:** 19 story points (US1 to US5)

| Story | Tasks | Owner |
|-------|-------|-------|
| US1 | Create `Library.add_book`, POST /books endpoint, validation, unit tests | Student 1 |
| US2 | Create `Library.search`, GET /books?q= endpoint, tests | Student 2 |
| US3 | Create `issue_book` logic, POST /books/{id}/issue, error handling, tests | Student 1 |
| US4 | Create `return_book` logic, POST /books/{id}/return, tests | Student 2 |
| US5 | Write GitHub Actions workflow (build, test, quality, deploy), Dockerfile | Both |

**Sprint ceremonies:** Sprint Planning (Day 1), short daily stand-up, Sprint Review
(demo the pipeline), Sprint Retrospective (what went well, what to improve).

## 4. Definition of Done (DoD)
A story is **Done** only when:
1. Code is committed to GitHub and merged through the main branch.
2. Acceptance criteria are all met.
3. Unit and API tests are written and **all pass** in the pipeline.
4. Test coverage is **at least 80%**.
5. Code passes the **flake8** lint check with zero errors.
6. The pipeline's **Build, Test and Quality stages are green**.
7. The change is **deployed** (Docker image published) automatically from `main`.

## 5. Acceptance Criteria (for US3: Issue a Book)

**Scenario 1: Issue an available book**
- *Given* a book exists and is available
- *When* the librarian issues the book
- *Then* the system responds with status 200 and the book is marked `available: false`

**Scenario 2: Issue an already-issued book**
- *Given* a book is already issued
- *When* the librarian tries to issue it again
- *Then* the system responds with status 400 and the message "Book is already issued"

**Scenario 3: Issue a book that does not exist**
- *Given* no book with that ID exists
- *When* the librarian tries to issue it
- *Then* the system responds with status 400 and the message "Book not found"

## 6. CI/CD Workflow
```
GitHub (push) -> Build -> Automated Testing -> Code Quality Check -> Deployment
```
| Stage | What it does | Tool |
|-------|-------------|------|
| GitHub | Push or pull request to `main` triggers the pipeline | Git, GitHub |
| Build | Install dependencies, compile the app | pip, compileall |
| Automated Testing | Run unit and API tests with coverage | pytest, pytest-cov |
| Code Quality Check | Lint the code, enforce 80% coverage | flake8, coverage gate |
| Deployment | Build Docker image and publish to GitHub Container Registry (only on `main`) | Docker, GHCR |

Each stage runs only if the previous one succeeds (`needs:` in the workflow).
