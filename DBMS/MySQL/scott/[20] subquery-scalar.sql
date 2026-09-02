-- 서브쿼리
-- 스칼라 서브쿼리(scalar sub-query)
-- SELECT 절에서 칼럼의 결과를 SELECT로 기술
-- 칼럼의 하나의 열 영역의 결과를 SELECT로 기술
-- 조건:
--   -> SELECT절에 명시하는 서브 쿼리의 결과는 하나의 칼럼에 해당하는 값만 나와야 한다.
--   -> 다중행 결과가 나오면 안 된다.

use scott;

-- 급여 등급(호봉)
SELECT * FROM salgrade;

-- 사원별 급여 등급(join)
SELECT e.empno, e.ename, e.sal, s.grade
    FROM emp e, salgrade s
    WHERE e.sal BETWEEN s.losal AND s.hisal
    ORDER BY 4; -- 급여등급 순

-- ANSI SQL    
SELECT e.empno, e.ename, e.sal, s.grade
    FROM emp e JOIN salgrade s
    ON e.sal BETWEEN s.losal AND s.hisal
    ORDER BY 4; -- 급여등급 순
    

-- 스칼라 서브쿼리(scalar sub-query)
-- 14명 사원이 있지만 각 행에 대해서 
-- 사원 1명에 1개 행에 대응해서 
-- 급여등급(salgrade)은 1개의 행과 컬럼이 출력
SELECT e.empno, e.ename, e.sal, 
        (SELECT grade 
            FROM salgrade  
            WHERE e.sal BETWEEN losal AND hisal) as sgrade
    FROM emp e
    -- WHERE empno = 7369
    ORDER BY sgrade;
    
-- 스칼라 서브쿼리(scalar sub-query)
-- 리턴 행의 갯수가 1개 나와야 한다.
-- 오류: Subquery returns more than 1 row
SELECT grade FROM salgrade;  -- 5개 리턴
SELECT e.empno, e.ename, e.sal, 
        (SELECT grade FROM salgrade) as salgrade
    FROM emp e
    -- WHERE empno = 7369
    ORDER BY 4;
    
-- 칼럼의 값이 1개만 나와야 한다.
-- Error Code: 1241. Operand should contain 1 column(s)
SELECT e.empno, e.ename, e.sal, 
        (SELECT grade, losal, hisal -- 다중 컬럼?
            FROM salgrade
            WHERE e.sal BETWEEN losal AND hisal) as sgrade
    FROM emp e
    ORDER BY sgrade;    
        
-- [문제]
-- 스칼라 서브쿼리(scalar sub-query)를 이용해서
-- 사원별 급여등급과 부서이름 출력하라.




SELECT e.empno, e.ename, d.deptno, d.dname
    FROM emp e, dept d
    WHERE e.deptno = d.deptno;

SELECT e.empno, e.ename, e.sal, 
        (SELECT grade FROM salgrade WHERE e.sal BETWEEN losal AND hisal) as salgrade,
        (SELECT dname FROM dept WHERE e.deptno = deptno) as dname
    FROM emp e
    ORDER BY 5;    
    
SELECT e.empno, e.ename, e.sal, s.grade, d.deptno, d.dname
    FROM emp e, dept d, salgrade s
    WHERE e.deptno = d.deptno
    AND e.sal BETWEEN s.losal AND s.hisal;
    
