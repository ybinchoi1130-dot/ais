-- 조회: 함수 사용

SELECT * FROM emp;

-- 사원의 이름의 첫 글자만 대문자로 변환
-- left(ename, 1): 사원의 첫 글자만 추출
SELECT ename, left(ename, 1) FROM emp; 

-- 사원의 두 번째 글자부터 끝까지 추출
-- substring(문자열, 시작위치, [길이])
--   . 인덱스는 1부터 시작
--   . 길이: 추출할 문자열의 갯수, 생략하면 문자열 끝까지 추출
SELECT ename, 
	left(ename, 1),            -- 첫 글자 추출
    substring(ename, 2),       -- 두 번째부터 끝까지 추출
    lower(substring(ename, 2)) -- 소문자로 변환 
FROM emp; 

-- 최종 결과 : 이름의 첫 글자만 대문자로 변환하여 새로운 컬럼으로 출력
-- concat()  : 컬럼을 결합
-- AS 컬럼명 : 새로운 컬럼명 부여 
SELECT ename, 
	concat(left(ename, 1), lower(substring(ename, 2))) AS ename2
FROM emp; 
