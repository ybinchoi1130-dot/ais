
# 고객정보 예외 클래스 정의
class CustomerException(Exception):
    def __init__(self, code, name, msg=''):
        super().__init__(msg)
        self.code = code # 에러코드: -1:검색오류, -2:입력오류, -3:삭제오류
        self.name = name # 고객이름
        self.msg = msg   # 에러 메시지
        
    def code(self):
        return self.code
    
    def name(self):
        return self.name
    
    def info(self):
        error = "검색오류" if self.code == -1 \
            else "입력오류" if self.code == -2 \
            else "삭제오류" if self.code == -3 else "일반오류"
        print(f"[{error}] 고객이름:{self.name}, {self.msg}")
        

#%%

# 고객정보 클래스
class Customer:
    def __init__(self):
        self.customers = {} # dict: 고객정보 저장용
        
    def find(self, name):   # 검색: 고객정보, 고객명으로 검색
        tel = self.customers.get(name)
        if tel == None: # 고객정보가 없으면 예외발생
            raise CustomerException(-1, name, "해당 고객을 찾지 못함")
        return name, tel 
    
    def append(self, name, tel): # 추가: 고객정보(이름, 전화번호)
        val = self.customers.get(name)
        if val != None: # 이미 등록된 고객정보가 있으면 예외발생
            raise CustomerException(-2, name, "해당 고객이 이미 존재함")
        self.customers[name] = tel
        
    def delete(self, name): # 삭제: 고객정보(이름)
        tel = self.customers.get(name)
        if tel == None:
            raise CustomerException(-3, name, "해당 고객이 존재하지 않음")
            
        del self.customers[name]
        
    def list(self, title='전체목록'):
        print(f"[{title}] 총건수: {len(self.customers)}")
        for no, (name, tel) in enumerate(self.customers.items()):
            print(f"[{no}] {name} : {tel}")
        
#%%

cust = Customer()

try:
    cust.append("홍길동", "001") # 추가
    cust.append("전우치", "007") # 추가
    print('-' * 20)
    cust.list()     # 전체목록 출력
    print('-' * 20)
    print(cust.find("홍길동")) # 검색
    print(cust.find("전우치")) # 검색

    print('-' * 20)
    cust.list("전우치 지우기 전 목록")     # 전체목록 출력

    cust.delete('전우치')
    print(cust.find("양귀비")) # 검색(예외발생)
    print('-' * 20)
except CustomerException as e:
    e.info()
finally:
    print('-' * 20)
    cust.list("마지막 전체 목록")     # 전체목록 출력
    
    
    
