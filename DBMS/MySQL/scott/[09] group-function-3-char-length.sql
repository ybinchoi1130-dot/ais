-- 조회: 함수 사용
-- char_length: 보이는 글자수 그대로 
SELECT length('abc'), char_length('한글'), char_length('漢字') from dual;

--
SELECT * FROM scott.emp; 
SELECT ename, length(ename) from emp where length(ename) >= 4;
select length(''), char_length(' ') from dual;
SELECT ename, char_length(ename) from emp where char_length(ename) >= 4;