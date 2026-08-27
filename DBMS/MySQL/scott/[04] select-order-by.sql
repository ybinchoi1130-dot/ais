
-- 전체 조회
SELECT * FROM emp;

-- 사번 순으로 조회
-- 정렬: ORDER BY 컬럼명
SELECT * FROM emp ORDER BY empno; -- 오름차순

-- 내림차순: desc
SELECT * FROM emp ORDER BY empno desc;

-- 내림차순: 이름 순
SELECT * FROM emp ORDER BY ename desc;

-- 입사순서로 정렬: 가장 먼저 입사한 순서
SELECT * FROM emp ORDER BY hiredate;

-- 가장 급여를 많이 받는 순서로 정렬
SELECT * FROM emp ORDER BY sal desc;

-- 가장 급여를 많이 받는 순서로 정렬하고
-- 급여가 같으면 입사순서로 정렬하라.
-- asc: ascending(오름차순)
-- desc: descending(내림차순)
SELECT * FROM emp ORDER BY sal desc, hiredate asc;

-- 컬럼의 위치(순번)로 지정: 1부터 시작 
-- 순번: sal(6), hiredate(5)
SELECT * FROM emp ORDER BY 6 desc, 5 asc;


