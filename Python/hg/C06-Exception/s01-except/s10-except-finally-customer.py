# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:54:19 2024

@author: Solero
"""

# 고객 이름 관리 (이름,전화번호)
# 고객 정보검색 함수로 정의 
# 예외클래스 고객정보를 찾지못함
# 고객정보: 추가 ,삭제(옵션)
#%%
#예외 클래스
class CustomerException(Exception):
    def __init__(self,code,name,msg=''):
        super().__init__(msg)
        self.code = code
        self.name = name
        self.msg = msg
    
    def code(self):
        return self.code
    
    def name(self):
        return self.name
    
    def info(self):
        error = "검색오류" if self.code == -1 \
            else "입력오류" if self.code == -2 \
            else "삭제오류" if self.code == -3 else "일반오류"
        print(f"{error} 고객이름: {self.name}, {self.msg}")
       
#%%
#고객 정보 클래스
class Customer:
    def __init__(self):
        self.customer_list = {} #dict
    
    def find(self,name):
        tel = self.customer_list.get(name)
        if tel == None:
            raise CustomerException(-1, name,"해당 고객님을 찾지 못함")
        return name,tel
    
    def append(self,name,tel):
        val = self.customer_list.get(name)
        if val != None:
            raise CustomerException(-2, name,"해당 고객님이 이미 존재함")
        self.customer_list[name] = tel
    
    def delete(self,name):
        tel=self.customer_list.get(name)
        if tel == None:
            raise CustomerException(-3, name, "해당 고객님이 존재하지 않음")
            
        del self.customer_list[name]
        
        
    def list(self, title='전체목록'):
        print(f"[{title}] 총건수: {self.customer_list}")
        for no, (name, tel) in enumerate(self.customer_list.items()):
            print(f"[{no}] {name} : {tel}")

cust = Customer()

try:
    cust.append("홍길동", "001")
    cust.append("전우치", "007")
    print('-' * 20)
    cust.list()
    print('-' * 20)
    print(cust.find("홍길동"))
    print(cust.find("전우치"))
    cust.delete("홍길동")
    print(cust.find("양귀비"))
    print('-'*20)
    
except CustomerException as e:
    e.info()
    
finally:
    print('-'*20)
    cust.list("마지막 전체목록")