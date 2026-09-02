-- CHAPTER 07 서브쿼리(SUB QUERY)
-- 다중행 서브 쿼리: 쿼리 결과가 여러개의 행인 경우
-- IN, SOME, ANY, ALL, EXISTS

-- EXISTS
-- EXISTS는 서브쿼리의 결과가 존재하는지(단 한 건이라도 반환하는지)를 확인하는 연산자
-- 서브쿼리가 한 건 이상의 결과를 반환하면 TRUE
-- 아무 결과도 반환하지 않으면 FALSE
-- 주로 메인 쿼리의 컬럼을 서브쿼리 내부에서 참조하는 상관 서브쿼리(Correlated Subquery) 형태로 많이 사용

-- 사원을 가지고 있는 부서 정보 (EXISTS)
-- IN을 사용했을 때(SELECT * FROM dept WHERE deptno IN (...))와 동일한 결과
-- 부서(dept) 테이블의 각 행마다 해당 부서번호를 가진 사원이 emp 테이블에 존재하는지 확인

-- IN과 EXISTS의 차이점
-- IN: 
--   서브쿼리를 먼저 전부 실행해서 결과 목록을 만든 후, 
--   메인 쿼리의 값이 그 목록 안에 있는지 검사
-- EXISTS: 
--   메인 쿼리의 데이터 한 건 한 건에 대해 서브쿼리를 실행하면서, 
--   조건에 맞는 데이터가 발견되는 즉시 검사를 멈추고 참(TRUE)을 반환
--   데이터가 많을 때 성능상 더 유리한 경우가 많음

use scott;
-- EXISTS: 서브쿼리의 결과가 1건이라도 존재하면 TRUE
-- 소속된 사원이 있는 부서: 10, 20, 30
SELECT empno, 1 FROM emp e, dept d WHERE e.deptno = d.deptno;

SELECT * 
    FROM dept d
    WHERE EXISTS (SELECT 1 FROM emp e WHERE e.deptno = d.deptno);

-- 사원을 가지고 있지 않은 부서 정보 (NOT EXISTS)
-- NOT IN을 사용했을 때와 동일한 결과
-- emp 테이블에 해당 부서번호를 가진 사원이 아예 존재하지 않는 경우만 통과

-- NOT EXISTS: 서브쿼리의 결과가 존재하지 않으면 TRUE
-- 사원이 존재하지 않는 부서: 40
SELECT * 
    FROM dept d
    WHERE NOT EXISTS (SELECT 1 FROM emp e WHERE e.deptno = d.deptno);
    
    
-- 스칼라 서브쿼리
-- 리턴 행의 갯수가 1개가 나와야 한다.
select e.empno, e.ename, e.sal,
		(select grade from salgrade where e.sal between losal and hisal) as salgrade -- 스칼라 서브쿼리
        from emp e
        order by 4;
        
SELECT 
    e.empno, 
    e.ename, 
    (SELECT d.dname 
     FROM dept d 
     WHERE d.deptno = e.deptno) AS department_name
FROM emp e;

SELECT e.empno, e.ename, 
    (SELECT d.dname FROM dept d WHERE d.deptno = e.deptno) AS department_name,
     (select grade from salgrade where e.sal between losal and hisal) as salgrade
FROM emp e;

select e.empno,e.ename,e.sal,s.grade,d.deptno,d.dname
	from emp e join dept d join salgrade s
    on e.deptno = d.deptno
    and e.sal between losal and s.hisal;
    
