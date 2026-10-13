# Contributing to MOMentum

Thanks for your interest in contributing! This guide will help you get started.

## Getting Started

### Prerequisites

- Python 3.10+
- Git

### Development Setup

```bash
# Fork and clone
git clone https://github.com/<your-username>/momentum.git
cd momentum

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment config
cp .env.example .env
# Edit .env with your API keys (optional — app works without them)

# Run the development server
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 to verify everything works.

## How to Contribute

### Reporting Bugs

1. Check [existing issues](https://github.com/gitswagata1/momentum/issues) first
2. Use the **Bug Report** issue template
3. Include steps to reproduce, expected vs. actual behavior, and your environment

### Suggesting Features

1. Open an issue using the **Feature Request** template
2. Describe the problem it solves and the proposed solution

### Submitting Code

1. **Fork** the repository
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```
3. **Make your changes** — keep commits focused and atomic
4. **Test locally** — make sure the app runs and your change works
5. **Push** and open a Pull Request against `main`

### Branch Naming

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feat/description` | `feat/export-mom-to-pdf` |
| Bug fix | `fix/description` | `fix/overdue-task-status` |
| Docs | `docs/description` | `docs/api-examples` |
| Refactor | `refactor/description` | `refactor/auth-middleware` |

## Coding Standards

### Python

- Follow [PEP 8](https://peps.python.org/pep-0008/) style
- Use type hints for function signatures
- Keep functions focused — one function, one job
- Use Pydantic schemas for request/response validation

### Frontend (Vanilla JS)

- No build step — keep it simple
- Use `const`/`let`, never `var`
- Document complex UI logic with brief comments

### Commits

- Use [Conventional Commits](https://www.conventionalcommits.org/):
  - `feat:` new feature
  - `fix:` bug fix
  - `docs:` documentation
  - `refactor:` code restructuring
  - `test:` adding tests
  - `chore:` maintenance

## Pull Request Process

1. Fill out the PR template completely
2. Link any related issues
3. Ensure the app runs without errors
4. Keep PRs focused — one feature or fix per PR
5. Be responsive to review feedback

## Need Help?

- Browse issues tagged [`good first issue`](https://github.com/gitswagata1/momentum/labels/good%20first%20issue)
- Open a discussion or comment on an issue to ask questions
- Reach out to [@gitswagata1](https://github.com/gitswagata1)

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
