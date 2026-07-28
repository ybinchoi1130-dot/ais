# 문자열(string)

# ord(): ASCII 코드 값 확인
cr = ord('\r') # Carriage Return
lf = ord('\n') # Line Feed
ff = ord('\f') # Form Feed
ht = ord('\t') # Horizontal Tab
bs = ord('\b') # Backspace

# 10진수, 16진수
print(cr, hex(cr)) # 13(0x0d)
print(lf, hex(lf)) # 10(0x0a)
print(ff, hex(ff)) # 12(0x0c)
print(ht, hex(ht)) #  9(0x09)
print(bs, hex(bs)) #  8(0x08)

hello = "Hello"
world = "World"
print(f"{hello}{lf}{world}")      # Hello10World

# chr() : unicode 코드 문자 리턴
print(f"{hello}{chr(lf)}{world}") 
"""
Hello
World
"""
print(f"{hello}\n{world}") 
