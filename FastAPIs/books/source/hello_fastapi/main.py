from fastapi import FastAPI, status
from pydantic import BaseModel
app = FastAPI()

# 서버 실행: http://127.0.0.1:8000/
@app.get("/")
def root_handler():
    return {"message": "Hello, FastAPI!"}

# 경로 사용 : http://127.0.0.1:8000/login
@app.get("/login")
def login_handler():
    return {"message": "로그인 페이지에 오신 것을 환영합니다."}

# 경로 변수 사용
# http://127.0.0.1:8000/users/숫자
# 예: http://127.0.0.1:8000/users/1234
@app.get("/users/{user_id}")
def read_user_handler(user_id: int):
    return {"user_id": user_id, "message": f"사용자 {user_id} 정보 조회"}

# 쿼리 파라미터 사용
# http://127.0.0.1:8000/items?max_price=54000
@app.get("/items")
def read_items_handler(max_price: int | None = None):
    return {"max_price": max_price}

# 아이템 모델 정의
class Item(BaseModel):
    name: str
    price: int
    in_stock: bool = True

# 새 아이템 등록
"""
curl -X 'POST' \
  'http://127.0.0.1:8000/items' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "마우스",
  "price": 25000,
  "in_stock": true
}'
"""
@app.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
def create_item_handler(item: Item):
    print('[create_item_handler]', item)
    return item

# 변경(Update)
# 경로 변수, 쿼리 파라미터, 요청 본문 혼합 사용
# http://127.0.0.1:8000/items/1234?assignee=James
"""
curl -X 'PUT' \
  'http://127.0.0.1:8000/items/1234?assignee=James' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "price": 0,
  "in_stock": true
}'
"""
@app.put("/items/{item_id}")
def update_item_handler(item_id: int, assignee: str, item: Item):
    print('[update_item_handler]', item)
    return {
        "item_id": item_id,
        "assignee": assignee, # 담당자 또는 작업자
        "item": item
    }

# 주문 응답 모델
class OrderResponse(BaseModel):
    order_id: int
    pickup: bool | None = None

# 단일 주문 조회
# http://127.0.0.1:8000/orders/1234567?pickup=true
@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order_handler(order_id: int, pickup: bool | None = None):
    return {
        "order_id": order_id,
        "pickup": pickup,
    }