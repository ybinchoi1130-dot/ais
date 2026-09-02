-- 서브쿼리(sub-query)

-- [문제]
-- 전체 사원의 평균 급여보다 같거나 많은 급여를 받는 사원정보와 부서정보

-- 평균급여
select avg(sal) from emp; # 2073.214286

select e.empno, e.ename, e.sal, d.dname
	from emp e, dept d
	where e.deptno = d.deptno
	and e.sal >= (select avg(sal) from emp)
	order by e.sal;

-- ANSI SQL	
select e.EMPNO, e.ename, e.sal, d.dname
	from emp e join dept d
	on e.deptno = d.deptno
		and e.sal >= (select avg(sal) from emp)
	order by e.sal;
