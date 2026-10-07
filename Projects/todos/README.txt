[todos]

(프로젝트)
1. 프로그래밍 언어: 파이썬 3.13.14
2. 웹 프레임워크: FastAPI, Jinja2, Swagger
3. 데이터베이스: MySQL
    - 데이터베이스이름: fastapi_db
    - 사용자 아이디: fastapi
    - 비밀번호: fastapi
4. 인증: JWT

(파이썬 가상환경)
anaconda3: ais

(requestments.txt)
fastapi[standard]==0.128.0
sqlalchemy
pymysql
pwdlib[argon2]
itsdangerous
pyjwt
uvicorn
Jinja2

(개발 단계에서 실행)
fastapi dev app/main.py

(서비스 단계에서 실행)
uvicorn app.main:app --reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080 

