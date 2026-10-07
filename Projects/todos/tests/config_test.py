# config.py 참조

import sys
from pathlib import Path

# 프로젝트 루트 경로(todos)를 sys.path에 추가
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from app.configs.config import settings

google_api_key=settings.GOOGLE_API_KEY,
print(google_api_key)

database_url=settings.DATABASE_URL,
print(database_url)
