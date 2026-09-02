# 서브쿼리(sub-query)

select * from emp; 
select * from emp where empno = 7654; -- 'MARTIN'
select sal from emp where empno = 7654; -- 1250

# 'MARTIN'의 급여보다 급여를 많이 받는 사원
# 'MARTIN'의 급여 : 1250
select * from emp where sal > 1250;

# [문제]
# 'MARTIN'의 사번을 이용해서 'MARTIN'의 급여보다 급여를 많이 받는 사원을 구하라.
select * from emp
	where sal > (select sal from emp where empno = 7654)
	order by sal;

-- [문제] 조인(join), 서브쿼리(subquery)
-- 부서코드가 20,30에 속한 사원중에서 TURNER(7844)보다 높은 급여(1,500)를 받는
-- 사원정보와 소속부서 정보를 출력
select sal from emp where empno = 7844;  -- 'TURNER' -> 1500.00

select * 
	from emp e, dept d        -- 조인
	where e.deptno in (20,30) -- 사원의 부서코드
	and e.deptno = d.deptno   -- 사원의 부서코드와 부서의 부서코드
	and e.sal > (select sal from emp where empno = 7844)
	order by e.sal;  -- 정렬
    
-- ANSI SQL    
-- 추천: JOIN ON을 함께 사용하는 것을 추천
select * 
	from emp e join dept d    -- 조인
	on e.deptno = d.deptno    -- 사원의 부서코드와 부서의 부서코드
	where e.deptno in (20,30) -- 사원의 부서코드
	and e.sal > (select sal from emp where empno = 7844) -- 'TURNER' -> 1500.00
	order by e.sal;  -- 정렬

select * 
	from emp e join dept d        -- 조인
	where e.deptno in (20,30)     -- 사원의 부서코드
	and e.deptno = d.deptno       -- 사원의 부서코드와 부서의 부서코드
	and e.sal > (select sal from emp where empno = 7844) -- 'TURNER' -> 1500.00
	order by e.sal;  -- 정렬


############################################################### 
# 급여등급
############################################################### 
select * from salgrade;

/*
1:   700 ~ 1200
2:  1201 ~ 1400
3:  1401 ~ 2000
4:  2001 ~ 3000
5:  3001 ~ 9999*/

# 사원의 급여등급
# 사원의 급여가 급여등급의 어떤 범위에 속해 있는가?
select e.EMPNO, e.ENAME, e.SAL, s.GRADE 
	from emp e, salgrade s
	where e.sal between s.LOSAL and s.HISAL;
    
# ANSI SQL    
select e.EMPNO, e.ENAME, e.SAL, s.GRADE 
	from emp e join salgrade s
	on e.sal between s.LOSAL and s.HISAL;

# TURNER(7844)의 급여 등급
select e.EMPNO, e.ENAME, e.SAL, s.GRADE 
	from emp e, salgrade s
	where e.EMPNO = 7844 # TURNER
	and e.sal between s.LOSAL and s.HISAL;

-- ANSI SQL    
select e.EMPNO, e.ENAME, e.SAL, s.GRADE 
	from emp e join salgrade s
	on e.EMPNO = 7844 # TURNER
	and e.sal between s.LOSAL and s.HISAL;
    
    
