-- 그룹함수
-- group by 

SELECT * FROM emp;
SELECT count(*) FROM emp;     -- 전체 행의 건수: 14건
SELECT count(empno) FROM emp; -- 전체 사번의 건수: 14건

-- NULL은 연산에서 제외
SELECT count(comm) FROM emp;  -- 수당(comm)을 받는 사람의 건수: 4건

-- empno: 단일행
-- count(*): 그룹핑
SELECT empno FROM emp;      -- 14개의 행이 추출: 사번목록 14개
SELECT count(*) FROM emp;   -- 1개의 행이 추출: 한 건(14)

-- 오류발생: 
-- 행의 갯수가 일치하지 않으므로 
-- empno 옆에 어떤 값을 매치해야 할지 판달할 수 없다.
SELECT empno, count(*) FROM emp;

-- 사원의 급여총액, 평균급여, 최대급여, 최소급여
SELECT 
	sum(sal), -- 총합
	avg(sal), -- 평균
    max(sal), -- 최댓값
    min(sal)  -- 최솟값
FROM emp;

-- 직책(job)의 갯수
-- DISTINCT: 중복 제거
SELECT DISTINCT job FROM emp; -- CLERK, SALESMAN, MANAGER, ANALYST, PRESIDENT

-- 사원의 직책(job)의 갯수
SELECT count(job) FROM emp; -- 14건, 총 사원수
SELECT count(distinct job) FROM emp; -- 5건, 

-- 사원의 직책별 건수
SELECT job, count(*) FROM emp GROUP BY job;
SELECT job, count(job) FROM emp GROUP BY job;

-- 사원의 부서별 사원수
SELECT deptno, count(deptno) FROM emp GROUP BY deptno;

-- 사원의 부서별 평균 급여
SELECT deptno, avg(sal) FROM emp GROUP BY deptno;

SELECT avg(sal) FROM emp GROUP BY deptno;
	
-- 부서별, 직책별 사원수    
SELECT deptno, job, count(*) as "사원수"
	FROM emp
    GROUP BY deptno, job  -- 그룹핑
    ORDER BY deptno, job; -- 정렬(sort): 오름차순

-- 부서별, 직책별 평균급여
SELECT deptno, job, avg(sal) as "평균급여"
	FROM emp
    GROUP BY deptno, job  -- 그룹핑
    ORDER BY deptno, job; -- 정렬(sort): 오름차순

-- 부서별, 직책별 사원수, 평균급여
SELECT deptno, job, count(*) as "사원수", avg(sal) as "평균급여"
	FROM emp
    GROUP BY deptno, job  -- 그룹핑
    ORDER BY deptno, job; -- 정렬(sort): 오름차순
    
-- 최근에 입사한 사원과 입사한지 가장 오래된 사원의 입사일
SELECT 
	max(hiredate) as "신참입사일", -- "1987-07-13"
	min(hiredate) as "고참입사일"  -- "1980-12-17"
FROM emp;

-- 최근에 입사한 사원과 입사한지 가장 오래된 사원의 입사일의 기간
-- 결과(일수): 2399, 6.5726
SELECT 
	DATEDIFF(max(hiredate), min(hiredate)) AS "일수",
	DATEDIFF(max(hiredate), min(hiredate)) / 365 AS "년수"
FROM emp;

