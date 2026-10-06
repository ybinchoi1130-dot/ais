from fastapi import APIRouter, status, HTTPException, Depends, BackgroundTasks
from sqlalchemy import select
from schema.request import UserSignUpRequest, UserLoginRequest
from database.db_connection import SessionFactory, get_session
from models import User
from auth.password import hash_password, verify_password
from schema.response import UserSignUpResponse
from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth.jwt import create_access_token, decode_access_token
router = APIRouter(tags=["User"])
bearer = HTTPBearer(auto_error=False)

# 회원가입 환영 메시지 출력
def send_welcome_email(email: str):
    import time
    time.sleep(5)
    print(f"Send welcome email to {email}...")

# 회원가입
@router.post(
    "/users/signup",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSignUpResponse
)
def signup_user_handler(
    body: UserSignUpRequest,
    background_tasks: BackgroundTasks,
    session=Depends(get_session)
):
    # with SessionFactory() as session:
    stmt = select(User).where(User.email == body.email)
    existing_user = session.scalar(stmt)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 사용 중인 이메일입니다."
        )
    hashed_password = hash_password(body.password)
    user = User(
        email=str(body.email),
        hashed_password=hashed_password,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    # 백그라운드 태스크 등록
    background_tasks.add_task(send_welcome_email, user.email)
    return user

# # 로그인(세션 방식)
# @router.post(
#     "/users/login",
#     status_code=status.HTTP_200_OK
# )
# def login_user_handler(request: Request, body: UserLoginRequest):
#     with SessionFactory() as session:
#         stmt = select(User).where(User.email == body.email)
#         user = session.scalar(stmt)
#         if not user:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="이메일 또는 비밀번호가 올바르지 않습니다."
#             )
#         if not verify_password(body.password, user.hashed_password):
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="이메일 또는 비밀번호가 올바르지 않습니다."
#             )
#     request.session["user_id"] = user.id
#     return {"message": "로그인 성공"}

# 로그인(JWT 방식)
@router.post("/users/login", status_code=status.HTTP_200_OK)
def login_user_handler(
    body: UserLoginRequest,
    session=Depends(get_session)
):
    # with SessionFactory() as session:
    stmt = select(User).where(User.email == body.email)
    user = session.scalar(stmt)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일 또는 비밀번호가 올바르지 않습니다."
        )
    if not verify_password(body.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일 또는 비밀번호가 올바르지 않습니다."
        )
    access_token = create_access_token(user_id=user.id, expires_minutes=60)
    return {"access_token": access_token, "email": user.email}

# 현재 로그인 사용자 정보 조회
@router.get("/users/me", status_code=status.HTTP_200_OK)
def get_me_user_handler(
    session=Depends(get_session),
    authorization: HTTPAuthorizationCredentials | None = Depends(bearer)
):
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="인증되지 않은 사용자입니다."
        )
    user_id = decode_access_token(authorization.credentials)
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="사용자를 찾을 수 없습니다."
        )
    return {"id": user.id, "email": user.email}

# 로그아웃
@router.post(
    "/users/logout",
    status_code=status.HTTP_200_OK
)
def logout_user_handler(request: Request):
    # request.session.clear()
    return {"message": "로그아웃 완료"}
