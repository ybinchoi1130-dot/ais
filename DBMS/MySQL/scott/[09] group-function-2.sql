-- 그룹함수
-- 그룹함수 결과 제한

-- 부서별 급여 총액(sum)
SELECT deptno, sum(sal) as totsal
	FROM emp
    GROUP BY deptno
    ORDER BY totsal;
    
-- 부서별 급여 총액이 9000 이상인 부서
SELECT deptno, sum(sal) as totsal
	FROM emp
    GROUP BY deptno
    HAVING sum(sal) >= 9000 -- 그룹 계산된 결과에 대한 조건
    ORDER BY totsal;

SELECT deptno, sum(sal) as totsal
	FROM emp
    GROUP BY deptno
    HAVING totsal >= 9000 -- 그룹 계산된 결과에 대한 조건
    ORDER BY totsal;

-- 직책(job)이 'MANAGER'를 제외하고
-- 급여 총액이 5000 이상인 직책별 급여 총액과 총사원수
SELECT job, 
		sum(sal) as totsal,
		count(*) as "총사원수"
	FROM emp
	-- WHERE job NOT LIKE '%MANAGER%'
	WHERE job != 'MANAGER'  -- 같지 않다('MANAGER'를 제외)
    GROUP BY job
    HAVING totsal >= 5000
    ORDER BY totsal;

    