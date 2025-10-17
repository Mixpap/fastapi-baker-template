# FastAPI Baker Template

A [Baker](https://github.com/aliev/baker) template for generating modern FastAPI projects with optional database support and best practices.

## Features

- 🚀 **FastAPI** - Modern web framework with automatic API docs
- 📦 **UV** - Fast Python package manager (replaces pip/requirements.txt)
- 🗄️ **Optional Database** - SQLModel + Alembic with SQLite or PostgreSQL
- 🧹 **Ruff** - Lightning-fast linting and formatting
- ✨ **Typos** - Spell checking for code and documentation
- 🧪 **Pytest** - Testing framework with async support
- 🤖 **GitHub Copilot** - Pre-configured instructions for better AI assistance
- 🔧 **VS Code** - Optimized workspace settings and extensions
- ⚙️ **Smart Setup** - Conditional features based on your choices

## Usage

### Prerequisites
```bash
# Install Baker (project generator, see https://github.com/aliev/baker on how to install)

# Install UV (Python package manager)  
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Generate Project
```bash
baker fastapi-baker-template my-awesome-api
```

You'll be prompted to choose:
- ✅ **Database support** (SQLModel + Alembic)
- ✅ **Database type** (SQLite or PostgreSQL) 
- ✅ **Example CRUD endpoints** (User/Post models)
- ✅ **Logfire integration** (Enhanced logging)

### What Happens Automatically (if the hooks are executed)
1. **Template Generation** - Files created based on your choices
2. **Git Repository** - Initialized with proper .gitignore
3. **Virtual Environment** - UV creates and configures venv
4. **Dependencies** - All packages installed automatically
5. **Database Setup** - Migration structure ready (if selected)
6. **Code Quality** - Pre-configured linting and formatting

### Quick Start (Generated Project)
```bash
cd my-awesome-api

# If you chose database support:
uv run alembic revision --autogenerate -m "Initial migration"
uv run alembic upgrade head

# Start development server
uv run fastapi dev backend/main.py
```

Visit http://localhost:8000/docs for interactive API documentation.

## Generated Project Structure

```
my-awesome-api/
├── backend/
│   ├── main.py              # FastAPI application entry point
│   ├── deps.py              # Dependency injection (DB sessions, etc.)
│   ├── db/                  # Database layer (if selected)
│   │   ├── schema.py        # SQLModel database models
│   │   └── migrations/      # Alembic migration files
│   ├── routes/              # API route definitions
│   │   └── api.py           # Main API endpoints
│   ├── services/            # Business logic layer
│   │   └── example.py       # Example service patterns
│   └── tests/               # Test files with pytest
├── pyproject.toml           # UV dependencies and tool config
├── alembic.ini              # Database migration configuration (if DB selected)
├── .env.example             # Environment variable template
├── .vscode/                 # VS Code workspace settings
├── .github/                 # Copilot instructions and workflows
├── .gitignore               # Git ignore patterns
└── README.md                # Project-specific documentation
```

## Template Features

### Conditional Database Support
- **SQLModel** - Type-safe ORM with Pydantic integration
- **Alembic** - Professional database migration management
- **Multi-DB** - SQLite (development) or PostgreSQL (production) [PostgreSQL has not been tested yet]
- **CRUD Examples** - Optional User/Post relationship models

### Modern Python Tooling
- **UV Package Manager** - 10-100x faster than pip
- **Ruff** - All-in-one linting, formatting, and import sorting
- **Typos** - Catches spelling mistakes in code and docs
- **Pytest** - Async-ready testing with coverage support

### Developer Experience
- **FastAPI** - Automatic OpenAPI docs and type validation
- **GitHub Copilot** - Context-aware AI assistance configuration
- **VS Code** - Optimized settings and recommended extensions
- **Hot Reload** - Instant server restarts during development

## Development Commands (Generated Project)

```bash
# Start development server
uv run fastapi dev backend/main.py

# Run tests
uv run pytest

# Database migrations (if DB enabled)
uv run alembic revision --autogenerate -m "description"
uv run alembic upgrade head

# Code quality
uv run ruff format      # Format code
uv run ruff check --fix # Fix linting issues
uv run typos           # Check spelling
```

## Contributing to Template

To modify this template:
1. Edit the `.baker.j2` template files
2. Update `baker.yaml` for new configuration options
3. Test generation: `baker . test-project`
4. Submit PR with your improvements

## ⚠️ LLM Assistance usage
Some of the code in this template was generated with the help of large language models (LLMs) and have not been fully tested and reviewed. Please review and test thoroughly before using in production.