from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database.db_connection import engine
from database.orm import Base
from routers.todo import router as todo_router
from routers.user import router as user_router
from routers.web import router as web_router
# from starlette.middleware.sessions import SessionMiddleware
from contextlib import asynccontextmanager

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

@asynccontextmanager
async def lifespan(_):
    Base.metadata.create_all(bind=engine)
    yield
    
app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "web" / "static")), name="static")

app.include_router(todo_router)
app.include_router(user_router)
app.include_router(web_router)

"""
app.add_middleware(
    SessionMiddleware,
    secret_key="your-secret-here"
)
"""