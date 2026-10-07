from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs.config import settings
# 데이터베이스 연결 정보 설정
DATABASE_URL = "mysql+pymysql://fastapi:fastapi@localhost:3306/fastapi_db"
# DATABASE_URL = settings.DATABASE_URL,

# 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)

# 세션 팩토리 생성
SessionFactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine,
)

# 세션 생성
def get_session():
    with SessionFactory() as session:
        yield session