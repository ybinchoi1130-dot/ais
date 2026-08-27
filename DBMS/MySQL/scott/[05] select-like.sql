-- 조회: LIKE
-- 함수: LOWER, UPPER

-- 전체 컬럼
SELECT * FROM emp;

-- 사번, 이름, 급여
SELECT empno, ename, sal FROM emp;

-- 이름 검색: 사번, 이름
SELECT empno, ename FROM emp WHERE ename = 'JONES';
SELECT empno, ename FROM emp WHERE ename = 'JAMES';

-- 이름이 'JONES', 'JAMES'인 사원
SELECT empno, ename FROM emp WHERE ename IN('JONES', 'JAMES');


-- 소문자로 검색: 구분하지 않음
-- CREATE DATABASE scott DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
SELECT empno, ename FROM emp WHERE ename = 'james';

-- 옵션: BINARY
-- 대소문자를 구분해서 검색: 검색 되지 않음
SELECT empno, ename FROM emp WHERE ename = BINARY 'james';

-- 조회 컬럼을 소문자로 변환하여 검색
SELECT lower(ename) FROM emp;
SELECT empno, ename FROM emp WHERE lower(ename) = BINARY 'james';

-- 검색하는 값을 대문자로 변환
SELECT upper('james');           -- dual 생략 가능
SELECT upper('james') FROM dual; -- 특정 테이블을 명시하지 않고 실행
SELECT empno, ename FROM emp WHERE ename = BINARY UPPER('james');

-- LIKE: 임의의 문자와 매칭
-- 이름이 'J%'로 시작하는 사원
SELECT empno, ename FROM emp WHERE ename LIKE 'J%';

-- 이름이 '%S'로 끝나는 사원: JONES, ADAMS, JAMES
SELECT empno, ename FROM emp WHERE ename LIKE '%S';

-- 이름이 'J'로 시작하고 'S'로 끝나는 사원: JONES, JAMES
SELECT empno, ename FROM emp WHERE ename LIKE 'J%S';

-- 이름이 'J'로 시작하고 전체 자릿수가 5자리이며 '
SELECT empno, ename FROM emp WHERE ename LIKE 'J____';

-- 이름이 'J'로 시작하고 2자리는 임의의 문자뒤에
-- 'E'가 포함되고 임의의 문자로 구성된 사원
SELECT empno, ename FROM emp WHERE ename LIKE 'J__E%';

