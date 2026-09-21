# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:00:40 2026

@author: shyun
"""

# python .\async_demo_1.py

import asyncio

# async 키워드를 사용하여 비동기 함수 정의 (이 부분은 import가 없어도 문법상 유효함)
async def main():
    print("Hello")
    # asyncio.sleep을 통해 1초 대기 (비동기 작업 시뮬레이션)
    await asyncio.sleep(1)
    print("Async World!")

# asyncio.run()을 사용하여 이벤트 루프를 생성하고 비동기 함수를 실행
asyncio.run(main())

print("THE END")

#%%

"""
결과:
Hello
Async World!
THE END
"""