# 제어문(if)
# None은 참(True)이 아니다.
# None은 거짓(False)이 아니다.
# None은 아무것도 없다는 의미의 특별한 값.

thing = None

if thing == True:
    print('Thing is True')
elif thing == False:
    print('Thing is False')    
elif thing == None:
    print('Thing is None')     # 해당  
else:
    print('Thing is Unknown')    
    
# 결과 : Thing is None    