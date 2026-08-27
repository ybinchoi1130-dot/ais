-- 최종 결과 : 이름의 첫 글자만 대문자로 변환하여 새로운 컬럼으로 출력
-- concat()  : 컬럼을 결합
-- concat()  : 문자열 결합도 가능
-- AS 컬럼명 : 새로운 컬럼명 부여 

-- 사원 이름의 첫 글자를 대문자로 바꾸고 나머지는 소문자로 변환 
SELECT ename, 
	concat(left(ename, 1), lower(substring(ename, 2))) AS ename2
FROM emp; 

SELECT concat('홍',' ','길동') from dual;
SELECT concat('홍길동') as '이름',
		  concat(2022,10,25) as '나이'
          from dual;
          
-- mysql에서는 (||) 논리연산자(or)로 동작
SELECT ('홍'  ||  '길동') as name from dual;

-- 주의 
-- 결합할때 null이 있으면 전체 결과가 null이 된다.
-- 결과: 수당(comm)이 있는 4건외에는 모두 null이 출력
SELECT concat(sal, ',' , comm) as '급여와 수당' from emp;

-- 구분자를 포함한 결합
-- concat_ws(구분자, 값1,값2 ...)
-- 결과: 급여와 수당 사이에 구분자를 넣어서 출력 
-- null이 있어도 출력된다.

 
SELECT concat_ws(',' , sal, comm) as '급여와 수당' from emp;
