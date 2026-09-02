-- 서브쿼리(sub-query)
-- 메인쿼리: 서브쿼리의 결과를 가지고 있는 쿼리
-- 서브쿼리:
--   1. 메인쿼리의 대상
--   2. 메인 쿼와 자료형과 컬럼의 갯수가 같아야 한다.
--   3. 단일행 서브 쿼리: 서브 쿼리의 결과가 하나인 경우
--      . 같다(=), 같지않다(!=), 크다(>), 작다(<), 크거나같다(>=), 작거나 같다(<=)
--   4. 다중행 서브 쿼리: 서브 쿼리의 결과가 여러개인 경우
--      . IN, SOME, ALL, ANY

-- 사원('JAMES')의 부서코드: 30
SELECT ename, deptno FROM emp WHERE ename = 'JAMES';

-- 사원('JAMES')의 부서코드(30)와 동일한 부서에서 근무하는 상원?
-- 서브쿼리의 결과 컬럼이 다중이면 안된다.
-- Error Code: 1241. Operand should contain 1 column(s)
-- SELECT * FROM emp WHERE deptno = (SELECT ename, deptno FROM emp WHERE ename = 'JAMES');
SELECT * FROM emp WHERE deptno = (SELECT deptno FROM emp WHERE ename = 'JAMES');

-- 사원('JAMES')보다 급여를 적게 받는 사원 : 950.00
SELECT ename, sal FROM emp WHERE ename = 'JAMES';
SELECT ename, sal FROM emp WHERE sal < 950; -- SMITH

SELECT * FROM emp WHERE sal < 950;
SELECT * FROM emp WHERE sal < 800;
SELECT * FROM emp WHERE sal <= (SELECT sal FROM emp WHERE sal < 950);
SELECT * FROM emp WHERE sal < (SELECT sal FROM emp WHERE ename = 'JAMES');

-- 
SELECT sal FROM emp WHERE ename = 'KING';  -- 5000
SELECT sal FROM emp WHERE sal < 5000;      -- 13명

-- 서브쿼리의 결과가 다중 행이 리턴하면 오류
-- Error Code: 1242. Subquery returns more than 1 row
-- SELECT * FROM emp WHERE sal < (SELECT sal FROM emp WHERE sal < 5000);

-- 급여가 3000보다 많이 받는 사원중에서
-- 가장 적게 받는 사원의 급여보다 더 적게 받는 사원은
SELECT * FROM emp WHERE sal < (SELECT min(sal) FROM emp WHERE sal > 3000);

-- 급여가 3000보다 많이 받는 사원중에서 가장 급여 많이 
-- 받는 사원보다 적게 받는 사원
SELECT * FROM emp WHERE sal < (SELECT max(sal) FROM emp WHERE sal > 3000);
