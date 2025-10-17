# Baker Template: Conditional Database Features

## Overview

This Baker template now supports conditional database functionality, allowing users to choose whether they want database features included in their FastAPI project.

## Baker Configuration

### New Questions in `baker.yaml`

```yaml
use_database:
  type: bool
  help: "Would you like to include database functionality with SQLModel?"
  default: true

database_type:
  type: str
  help: "Which database would you like to use?"
  choices: [sqlite, postgresql, mysql]
  default: sqlite
  when: use_database

include_db_examples:
  type: bool
  help: "Would you like to include example CRUD operations?"
  default: true
  when: use_database
```

## Template Files Created

### Core Templates (always needed)
- `backend/deps.py.baker.j2` - Dependencies with conditional database code
- `backend/routes/api.py.baker.j2` - API routes with optional CRUD examples
- `pyproject.toml.baker.j2` - Dependencies with conditional database packages
- `README.md.baker.j2` - Documentation with conditional database sections

### Conditional Templates (only when database enabled)
- `backend/db/schema.py.baker.j2` - Database models (only created if `use_database=true`)
- `docs/database.md.baker.j2` - Database documentation (only created if `use_database=true`)
- `.env.example.baker.j2` - Environment template with conditional DB config
- `backend/tests/test_deps.py.baker.j2` - Tests with conditional database tests

## How It Works

### 1. Conditional Imports
```jinja
{%- if use_database %}
from sqlmodel import Session, create_engine, SQLModel
{%- endif %}
```

### 2. Conditional Code Blocks
```jinja
{%- if use_database %}
def get_db_session() -> Generator[Session, None, None]:
    # Database session code here
{%- endif %}
```

### 3. Conditional Dependencies
```jinja
dependencies = [
    "fastapi[standard]>=0.104.0",
    {%- if use_database %}
    "sqlmodel>=0.0.14",
    {%- if database_type == "postgresql" %}
    "psycopg2-binary>=2.9.0",
    {%- elif database_type == "mysql" %}
    "pymysql>=1.0.0",
    {%- endif %}
    {%- endif %}
]
```

### 4. Database-Specific Configuration
```jinja
{%- if database_type == "postgresql" %}
default="postgresql://user:password@localhost/{{project_name.lower()}}"
{%- elif database_type == "mysql" %}
default="mysql://user:password@localhost/{{project_name.lower()}}"
{%- else %}
default="sqlite:///./app.db"
{%- endif %}
```

## Generated Project Variations

### Option 1: No Database
User selects `use_database=false`:
- ✅ Basic FastAPI setup
- ✅ Health check endpoint
- ❌ No database dependencies
- ❌ No database models
- ❌ No CRUD examples

### Option 2: SQLite with Examples  
User selects `use_database=true`, `database_type=sqlite`, `include_db_examples=true`:
- ✅ Full database setup with SQLite
- ✅ User/Post example models
- ✅ CRUD API endpoints
- ✅ Database documentation
- ✅ Ready to run (no external database needed)

### Option 3: PostgreSQL without Examples
User selects `use_database=true`, `database_type=postgresql`, `include_db_examples=false`:
- ✅ Database setup for PostgreSQL
- ✅ PostgreSQL driver included
- ✅ Empty schema file with comments
- ❌ No example models or endpoints
- 📋 Database setup instructions in docs

## Testing the Template

Use the provided test script:
```bash
./test_baker_template.sh
```

Or test manually:
```bash
baker create . my-test-project
# Follow the prompts to test different configurations
```

## File Structure After Generation

### Without Database (`use_database=false`)
```
my-project/
├── backend/
│   ├── deps.py          # No database code
│   ├── routes/api.py    # Basic endpoints only
│   └── tests/
├── pyproject.toml       # No database dependencies
└── README.md           # No database sections
```

### With Database (`use_database=true`)
```
my-project/
├── backend/
│   ├── deps.py          # Full database setup
│   ├── db/schema.py     # Database models
│   ├── routes/api.py    # CRUD endpoints (if examples enabled)
│   └── tests/
├── docs/database.md     # Database documentation
├── .env.example         # Database configuration
├── pyproject.toml       # Database dependencies included
└── README.md           # Database sections included
```

## Best Practices for Template Development

1. **Use `when` conditions** for dependent questions
2. **Group related conditional code** in blocks
3. **Provide clear defaults** for different scenarios
4. **Test all combinations** of options
5. **Document the variations** clearly
6. **Use meaningful variable names** in templates

## Adding New Conditional Features

To add new optional features:

1. **Add questions** to `baker.yaml`
2. **Update template files** with conditional blocks
3. **Create feature-specific templates** if needed
4. **Update documentation** and README
5. **Test all combinations**

Example for adding Redis caching:
```yaml
use_redis:
  type: bool
  help: "Would you like to include Redis caching?"
  default: false
```

Then in templates:
```jinja
{%- if use_redis %}
"redis>=4.0.0",
{%- endif %}
```