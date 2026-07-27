# 제어문(if)
# 조건부 표현식(conditional expression)

score = 80

# 역슬레시(\)로 한 문장을 여러줄로 기술할 수 있다.
# 역슬레시(\) 뒤에 스페이스를 포함 다른 문자가 오면 안된다.
msg = "A등급" if score >= 90 \
    else "B등급" if score >= 80 \
    else "C등급" if score >= 70 else "D등급"

print('msg=', msg)    
