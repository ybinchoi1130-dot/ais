-- 서브쿼리(sub-query)

-- [문제]
-- TURNER(7844)의 급여 등급에 속한 급여를 받는 사원 정보와 소속 부서 정보
-- TURNER(7844)의 급여 등급 : 3등급
-- 사원의 급여등급
select e.EMPNO, e.ENAME, e.SAL, s.GRADE 
	from emp e, salgrade s
	where e.sal between s.LOSAL and s.HISAL
	order by s.grade;
    
select e.EMPNO, e.ENAME, e.sal, e.DEPTNO, d.DNAME, s.GRADE 
	from emp e, dept d, salgrade s
	where e.DEPTNO = d.DEPTNO
	and (e.sal between s.LOSAL and s.HISAL)
	and s.grade = (select s.GRADE -- TURNER의 급여등급(3등급)
		from emp e, salgrade s
		where e.empno = 7844 and e.sal between s.losal and s.hisal)
	order by e.sal;

-- ANSI SQL
select e.EMPNO, e.ENAME, e.sal, e.DEPTNO, d.DNAME, s.GRADE 
	from emp e join dept d join salgrade s
	on (e.DEPTNO = d.DEPTNO
		and (e.sal between s.LOSAL and s.HISAL)
		and s.grade = (select s.GRADE -- TURNER의 급여등급(3등급)
			from emp e, salgrade s
			where e.empno = 7844 and e.sal between s.losal and s.hisal))
	order by e.sal;


