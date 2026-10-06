from fastapi import FastAPI
from database.db_connection import engine
from database.orm import Base
from routers.todo import router as todo_router
from routers.user import router as user_router

# 정의된 모델 기반으로 DB 테이블을 자동 생성
Base.metadata.create_all(bind=engine)

# FastAPI 애플리케이션 핵심 인스턴스 생성
app = FastAPI()

# 라우터 연결: todo 라우터
app.include_router(todo_router)

# 라우터 연결: user 라우터
app.include_router(user_router)
