---
applyTo: '**/*.py'
---

# FastAPI rules (Backend)
- For python environment we use the uv tool
- Use type hints for all function parameters and return values
- Use Pydantic models for request and response validation
- Use appropriate HTTP methods with path operation decorators (@app.get, @app.post, etc.)
- Use dependency injection for shared logic like database connections and authentication
- Use background tasks for non-blocking operations
- Use proper status codes for responses (201 for creation, 404 for not found, etc.)
- Use APIRouter for organizing routes by feature or resource
- Use path parameters, query parameters, and request bodies appropriately
- Use ruff for code formatting and linting (not black, flake8, or mypy)
- Use typos for spell checking (not separate spelling tools)
- Do not use complex or unnecessary code structures unless they add strong value on quality, maintainability, complexity or reusability. Avoid classes unless really needed.
- Write unit tests using pytest (not unittest)
- For logging use loguru module
- Always use polars instead of pandas
- Discuss any possible issues regarding scalability, security, reproducibility, safety etc
- Strongly avoid creating unnecessary files, directories and dependencies and making significant changes in the codebase
