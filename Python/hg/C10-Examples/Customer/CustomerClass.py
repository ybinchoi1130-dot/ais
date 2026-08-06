# 고객정보 클래스
class Customer:
    def __init__(self):
        self.customers = {}
        
    def find(self, name):
        tel = self.customers.get(name)
        if tel == None:
            raise CustomerException(-1, name, "해당 고객을 찾지 못함")
        return name, tel 
    
    def append(self, name, tel):
        val = self.customers.get(name)
        if val != None:
            raise CustomerException(-2, name, "해당 고객이 이미 존재함")
        self.customers[name] = tel
        
    def delete(self, name):
        tel = self.customers.get(name)
        if tel == None:
            raise CustomerException(-3, name, "해당 고객이 존재하지 않음")
            
        del self.customers[name]
        
    def list(self, title='전체목록'):
        print(f"[{title}] 총건수: {self.customers}")
        for no, (name, tel) in enumerate(self.customers.items()):
            print(f"[{no}] {name} : {tel}")
        