from pydantic import BaseModel

# 할 일 생성 요청 모델: POST
class TodoCreateRequest(BaseModel):
    title: str
    is_done: bool = False

# 할 일 변경 요청 모델: PUT, PATCH
class TodoUpdateRequest(BaseModel):
    title: str | None = None  
    is_done: bool | None = None