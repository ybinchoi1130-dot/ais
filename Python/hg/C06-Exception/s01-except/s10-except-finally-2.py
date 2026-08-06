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
customer_list = {}
class CustomerNOTFINDERROR(Exception):
    def __init__(self,name):
        super().__init__(f"오류 : '{name}'의 정보를 찾지 못합니다.")


def add_customer(name,phone):
    customer_list[name] = phone
    print(f"[등록완료] {name} : {phone}")

def search_customer(name):
    if name not in customer_list:
        raise CustomerNOTFINDERROR(name)
        
    return customer_list[name]

def delete_customer(name):
    if name not in customer_list:
        raise CustomerNOTFINDERROR(name)
        
    del customer_list[name]
    print(f"[삭제 완료] '{name}'의 정보가 삭제되었습니다.")

#%%

add_customer("홍길동", "010-1234-5678")
print(customer_list)

if __name__ == "__main__":
   try:
       phone = search_customer("홍길동")
       print(f"검색 결과:홍길동님의 번호는 {phone} 입니다.")
   except CustomerNOTFINDERROR as e:
        print(e)
   try:
       phone = search_customer("이순신")
       print(f"검색 결과:이순신님의 번호는 {phone} 입니다.")
   except CustomerNOTFINDERROR as e:
        print(e)
    
   try:
       phone = delete_customer("홍길동")
       print(f"홍길동님의 정보를 삭제완료했습니다.")
   except CustomerNOTFINDERROR as e:
       print(e)
       
print(customer_list)
   