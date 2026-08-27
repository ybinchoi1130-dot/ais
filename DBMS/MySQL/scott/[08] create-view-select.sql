-- 기존의 테이블을 사용하여 새로운 뷰(View) 테이블을 생성
-- 뷰(View): 물리적인 테이블의 특정 검색 결과를
--           가지고 있는 가상의 테이블

-- 검색 결과로 새로운 뷰 테이블을 생성
CREATE OR REPLACE VIEW emp_vw AS SELECT * FROM emp;

SELECT * FROM emp_vw WHERE empno = 9999; -- 'SOPIA'

-- 뷰 삭제
DROP VIEW emp_vw;

-- 사용자 이름: 첫 번째 문자만 대문자로 변경하고 나머지는 소문자
CREATE VIEW emp_vw AS
	SELECT empno, 
		concat(left(ename, 1), lower(substring(ename, 2))) AS ename,
        job, mgr, hiredate, sal, comm, deptno
	FROM emp;
    
SELECT * FROM emp_vw;

INSERT INTO emp 
	VALUES(8888, 'PIG', 'CLERK', 7902, '2020-10-10', 1600, NULL, 20);

-- 합집합  
SELECT * FROM emp WHERE empno = 8888      -- ename: PIG
UNION ALL
SELECT * FROM emp_vw WHERE empno = 8888;  -- ename: Pig

DELETE FROM emp WHERE empno IN (8888,9999);