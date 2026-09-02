-- 서브쿼리(sub-query)
-- 메인쿼리: 서브쿼리의 결과를 가지고 있는 쿼리
-- 서브쿼리:
--   1. 메인쿼리의 대상
--   2. 메인 쿼와 자료형과 컬럼의 갯수가 같아야 한다.
--   3. 단일행 서브 쿼리: 서브 쿼리의 결과가 하나인 경우
--      . 같다(=), 같지않다(!=), 크다(>), 작다(<), 크거나같다(>=), 작거나 같다(<=)
--   4. 다중행 서브 쿼리: 서브 쿼리의 결과가 여러개인 경우
--      . IN, SOME, ALL, ANY

-- IN
-- 서브 쿼리가 반환한 여러 행의 결과에서
-- 메인 쿼리의 조건식과 하나라도 같으면
-- 메인 쿼리는 TRUE를 반환한다.

-- 각 부서별 최저 급여액
SELECT deptno, min(sal) FROM emp GROUP BY deptno ORDER BY 2;
SELECT min(sal) FROM emp GROUP BY deptno ORDER BY 1;  -- 800, 950, 1300

-- 각 부서별 최저 급여액을 받는 사원
SELECT empno, ename, sal, deptno
	FROM emp
    WHERE sal IN (800, 950, 1300)
    ORDER BY sal;

-- 각 부서별 최저 급여액을 받는 사원
SELECT empno, ename, sal, deptno
	FROM emp
    WHERE sal IN (SELECT min(sal) FROM emp GROUP BY deptno)
    ORDER BY sal;

-- 각 부서별 최고 급여액을 받는 사원
SELECT empno, ename, sal, deptno
	FROM emp
    WHERE sal IN (SELECT max(sal) FROM emp GROUP BY deptno)
    ORDER BY sal;

-- 각 부서별 평균 급여액을 받는 사원: 없음
SELECT avg(sal) FROM emp GROUP BY deptno;
SELECT empno, ename, sal, deptno
	FROM emp
    WHERE sal IN (SELECT avg(sal) FROM emp GROUP BY deptno)
    ORDER BY sal;

-- 전체 부서 코드
SELECT distinct deptno FROM dept;  -- 4개 부서 존재: 10, 20, 30, 40

-- 사원들이 소속된 부서 코드
SELECT deptno FROM emp;            -- 모든 사원의 소속 부서: 14건
SELECT distinct deptno FROM emp;   -- 중복 제거: 10, 20, 30

-- 사원들이 소속된 부서 정보: 
-- 10, 20, 30만 선택
-- 40은 제외
SELECT * FROM dept
	WHERE deptno IN (SELECT distinct deptno FROM emp);

-- distinct를 기술하지 않아도 
-- 오류가 발생되지는 않지만 비효율 적이다.
SELECT * FROM dept
	WHERE deptno IN (SELECT deptno FROM emp);

-- 사원을 가지고 있는 않은 부서 정보: 40번 부서
SELECT * FROM dept
	WHERE deptno NOT IN (SELECT distinct deptno FROM emp);


