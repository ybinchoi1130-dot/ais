-- 최종 결과 : 이름의 첫 글자만 대문자로 변환하여 새로운 컬럼으로 출력
-- substring(),substr(): (문자열,시작위치,추출)

-- 사원 이름의 첫 글자를 대문자로 바꾸고 나머지는 소문자로 변환 
SELECT ename, 
	substring(ename, 1,1) AS ename2,
    substr(ename,1,1) as ename3
FROM emp; 

select '홍길동',
	substr('홍길동',1,1) as Lastname,
    substr('홍길동',2,2) as firstname
from emp;

-- mid도 동일하다. 

select '홍길동',
	mid('홍길동',1,1) as Lastname,
    mid('홍길동',2,2) as firstname
from emp;


