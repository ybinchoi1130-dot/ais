-- 서브쿼리(sub-query)
-- 메인쿼리: 서브쿼리의 결과를 가지고 있는 쿼리
-- 서브쿼리:
--   1. 메인쿼리의 대상
--   2. 메인 쿼와 자료형과 컬럼의 갯수가 같아야 한다.
--   3. 단일행 서브 쿼리: 서브 쿼리의 결과가 하나인 경우
--      . 같다(=), 같지않다(!=), 크다(>), 작다(<), 크거나같다(>=), 작거나 같다(<=)
--   4. 다중행 서브 쿼리: 서브 쿼리의 결과가 여러개인 경우
--      . IN, SOME, ALL, ANY

-- 부서(30)에서 가장 급여를 적게 받는 사원의 급여
(
	SELECT '10', min(sal) as minsal FROM emp WHERE deptno = 10
	UNION -- 합집합
	SELECT '20', min(sal) as minsal  FROM emp WHERE deptno = 20
	UNION -- 합집합
	SELECT '30', min(sal) as minsal  FROM emp WHERE deptno = 30
) ORDER BY minsal;

-- 각 부서별 최저 급여
SELECT deptno, min(sal) as minsal
	FROM emp
    GROUP BY deptno
    ORDER BY minsal;

-- [문제]
-- 부서(30)인 사원중에서 가장 급여를 적게 받는 사원보다 : 950
-- 급여를 많이 받는 사원들 중에서
-- 가장 급여를 적게 받는 사원의 부서별 최소 급여액
SELECT deptno, min(sal)
    FROM emp
    GROUP BY deptno
    HAVING min(sal) > (SELECT min(sal) FROM emp WHERE deptno = 30);

-- 부서(20)인 사원중에서 가장 급여를 적게 받는 사원보다 : 800
-- 급여를 많이 받는 사원들 중에서
-- 가장 급여를 적게 받는 사원의 부서별 최소 급여액
SELECT deptno, min(sal)
    FROM emp
    GROUP BY deptno
    HAVING min(sal) > (SELECT min(sal) FROM emp WHERE deptno = 20);

-- [문제]
-- 'TURNER'의 입사일자보다 빨리 입사한 사원
SELECT ename, hiredate FROM emp WHERE ename = 'TURNER'; -- '1981-09-08'
SELECT ename, hiredate 
    FROM emp 
    WHERE hiredate < (SELECT hiredate FROM emp WHERE ename = 'TURNER')
    ORDER BY hiredate;
    
-- [문제]
-- 'TURNER'의 입사일자보다 늦게 입사한 사원
SELECT ename, hiredate FROM emp WHERE ename = 'TURNER'; -- '1981-09-08'
SELECT ename, hiredate 
    FROM emp 
    WHERE hiredate > (SELECT hiredate FROM emp WHERE ename = 'TURNER')
    ORDER BY hiredate;

-- [문제]
-- 부서코드가 20에 속한 사원중에서 'TURNER'보다 높은 급여를 받는
-- 사원정보와 소속 부서 정보
SELECT * FROM emp WHERE ename = 'TURNER';  -- sal : 1500
SELECT *
    FROM emp e, dept d
    WHERE e.deptno = 20 AND e.deptno = d.deptno
    AND e.sal > (SELECT sal FROM emp WHERE ename = 'TURNER')
    ORDER BY e.sal;

SELECT *
    FROM emp e JOIN dept d
    ON e.deptno = 20 AND e.deptno = d.deptno
    AND e.sal > (SELECT sal FROM emp WHERE ename = 'TURNER')
    ORDER BY e.sal;

-- [문제]
-- 부서코드가 10,20에 속한 사원중에서 전체 사원 평균 급여보다 높은 급여를 받는
-- 사원정보와 소속 부서 정보
SELECT avg(sal) FROM emp;  -- 2073.214286
SELECT * 
	FROM emp e, dept d
    WHERE e.deptno IN (10,20)
    AND e.deptno = d.deptno
    AND e.sal > (SELECT avg(sal) FROM emp)
    ORDER BY e.sal;

SELECT * 
	FROM emp e JOIN dept d
    ON e.deptno IN (10,20)
    AND e.deptno = d.deptno
    AND e.sal > (SELECT avg(sal) FROM emp)
    ORDER BY e.sal;    