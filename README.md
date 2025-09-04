# FastAPI Template

A FastAPI project template with UV package manager and automated setup.

## Features

- 🚀 **FastAPI** - Modern web framework with automatic API docs
- 🤖 **GitHub Copilot** - pre-configured (personal preference) copilot instructions
- 📦 **UV** - Fast Python package manager (no requirements.txt)
- 🧹 **Ruff** - All-in-one linting and formatting
- ✨ **Typos** - Spell checking for code
- 🧪 **Pytest** - Testing framework with async support
- 🔧 **VS Code** - Pre-configured workspace settings
- ⚙️ **Automated Setup** - Post-generation hooks for instant dev environment

## Usage

### Generate Project
```bash
baker fastapi-template my-api-project
```

### What Happens Automatically
1. Project files generated from template
2. Git repository initialized
3. UV virtual environment created
4. Dependencies installed
5. Code formatted with Ruff
6. Ready to run!

### Start Development
```bash
cd my-api-project
uv run uvicorn backend.main:app --reload
```
or 
```
uv run fastapi devb backend/main.py 
```

Visit http://localhost:8000/docs for interactive API documentation.

## Template Structure

```
my-api-project/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── deps.py              # Dependencies
│   ├── routes/              # API routes
│   ├── services/            # Business logic
│   └── tests/               # Test files
├── pyproject.toml           # UV dependencies
├── .vscode/                 # VS Code settings
├── .github/                 # GitHub workflows and instructions
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## Development Commands

```bash
# Run server
uv run uvicorn backend.main:app --reload

# Run tests
uv run pytest

# Format code
uv run ruff format .

# Check code
uv run ruff check .

# Check spelling
uv run typos
```
