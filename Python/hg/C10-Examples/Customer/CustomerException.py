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
        