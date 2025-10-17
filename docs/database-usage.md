# Database Usage Guide

## Engine vs Session: Key Differences

### Engine
- **Purpose**: Connection pool manager and database interface
- **Lifecycle**: Created once at application startup, reused throughout app lifetime
- **Thread Safety**: Thread-safe, designed to be shared across multiple threads/requests
- **Usage**: Creates Sessions, executes raw SQL, manages database connections

### Session
- **Purpose**: Unit of work and transaction boundary
- **Lifecycle**: Created per request/operation, closed after use
- **Thread Safety**: NOT thread-safe - each thread/request needs its own Session
- **Usage**: ORM operations (queries, inserts, updates, deletes)

## FastAPI Best Practice: Use Session Dependencies

In FastAPI, **always pass the Session as a dependency**, not the Engine.

### Why Session Dependencies?
1. **Request Isolation**: Each request gets its own database session
2. **Transaction Management**: Sessions handle commits/rollbacks per request
3. **Connection Management**: Sessions automatically manage connections from the pool
4. **Error Handling**: Automatic rollback on exceptions

## Usage Examples

### 1. Basic CRUD Operations

```python
from fastapi import APIRouter
from ..deps import SessionDep
from ..db.schema import User

router = APIRouter()

@router.post("/users/")
async def create_user(user_data: UserCreate, db: SessionDep):
    """Create a new user."""
    user = User(name=user_data.name, email=user_data.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/users/")
async def get_users(db: SessionDep):
    """Get all users."""
    statement = select(User)
    users = db.exec(statement).all()
    return users
```

### 2. Complex Queries

```python
@router.get("/users/{user_id}/posts/")
async def get_user_posts(user_id: int, db: SessionDep):
    """Get all posts by a specific user."""
    statement = select(Post).where(Post.author_id == user_id)
    posts = db.exec(statement).all()
    return posts
```

### 3. Error Handling

```python
@router.get("/users/{user_id}")
async def get_user(user_id: int, db: SessionDep):
    """Get a specific user by ID."""
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"User with id {user_id} not found"
        )
    return user
```

## Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
DATABASE_URL=sqlite:///./app.db
# For PostgreSQL: postgresql://user:password@localhost/dbname
# For MySQL: mysql://user:password@localhost/dbname
```

### Database Settings

The database URL is configured in `Settings` class in `deps.py`:

```python
class Settings(BaseSettings):
    database_url: str = Field(
        default="sqlite:///./app.db",
        validation_alias="DATABASE_URL"
    )
```

## Transaction Management

The session dependency automatically handles:
- **Commit**: Changes are committed at the end of successful requests
- **Rollback**: Changes are rolled back if an exception occurs
- **Close**: Session is properly closed after each request

```python
def get_db_session() -> Generator[Session, None, None]:
    engine = get_db_engine()
    with Session(engine) as session:
        try:
            yield session
        except Exception:
            session.rollback()  # Automatic rollback on error
            raise
        finally:
            session.close()     # Always close the session
```

## Best Practices

1. **One Session per Request**: Never share sessions between requests
2. **Use the Dependency**: Always use `SessionDep` instead of creating sessions manually
3. **Let FastAPI Handle Lifecycle**: Don't manually commit/rollback unless needed
4. **Handle Exceptions**: Use proper HTTP status codes for database errors
5. **Use Type Hints**: Always type your dependencies properly

## Common Patterns

### Service Layer Pattern

```python
# In services/user_service.py
class UserService:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        user = User(**user_data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

# In routes/api.py
@router.post("/users/")
async def create_user(user_data: UserCreate, db: SessionDep):
    return UserService.create_user(db, user_data)
```