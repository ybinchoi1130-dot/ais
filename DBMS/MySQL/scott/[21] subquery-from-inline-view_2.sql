use scott;

select e.empno, e.ename, d.deptno, d.dname
	from emp e, dept d
    where e.deptno = d.deptno
    and e.deptno = 10;
 -- ANSI SQL
 select e.empno, e.ename, d.deptno, d.dname
	from emp e join dept d
    on e.deptno = d.deptno
    and e.deptno = 10;
    
select e.empno, e.ename, e.deptno, d.dname
	from (select empno,ename,deptno from emp where deptno =10) e,
		   (select dname from dept where deptno =10) d;
           
select e.empno, e.ename, e.deptno, d.dname
	from (select empno, ename, deptno from emp where deptno =10) e cross join
		   (select dname from dept where deptno =10) d;

-- 주의: 교차조인으로 인해서 from 절의 행의 결과가 2개 이상이면
-- 데이터가 중복해서 추출되므로 메인쿼리에서 한 번더 조인을 해야한다.
-- 데이터 중복되는 예시
select e.empno, e.ename, e.deptno, d.dname
	from (select empno,ename,deptno from emp where deptno in (10,30)) e,
		   (select dname from dept where deptno in (10,30)) d;
		
           