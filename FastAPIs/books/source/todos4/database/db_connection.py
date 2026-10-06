from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 데이터베이스 연결 정보 설정
# 데이터베이스: fastapi_db
# 사용자아이디: fastapi
# 사용자패스워드: fastapi
DATABASE_URL = "mysql+pymysql://fastapi:fastapi@localhost:3306/fastapi_db"

# 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

# 세션 팩토리 생성
SessionFactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
)