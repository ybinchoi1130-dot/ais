select date_format(now(),'%Y년%m월%d일 %W(%a)') from dual;

-- 날짜 / 시간 언어 설정
-- 한국어로 설정 
-- lc_time_names: 'ko_KR'

set lc_time_names = 'ko_KR';                                        
-- 영어로 설정
--  lc_time_names: 'en_US'
set lc_time_names = 'en_US';

set lc_time_names = 'ja_JP';


-- 요일 함수
-- dayofweek() : 일요일(1) -> 토요일(7)
-- weekday() : 월 (0) -> 일 (6)
select now() as "현재",
	dayofweek(now()) as "요일순번1",
    weekday(now()) as "요일순번0"
from dual;
-- 요일 함수 한글로 출력
-- ELT(순번,목록): 1부터시작
select now() as "현재",
	weekday(now()) as "요일순번0",
    elt(dayofweek(now()), '일','월','화','수','목','금','토') as "요일" 
from dual;
-- ELT에서 매칭되는 값을 찾지 못하면 기본값을 보여주라.

select
IFnULL(elt(4,'하나','둘','셋'), '없음')  as '순서' from dual;

-- 사원의 수당이 없으면 기본 수당으로 100 달러를 출력하라
select ename, comm, ifnull(comm,100) from emp;

-- 결과: 수당이 없으면 지급액은 급여(sal)만 반영된다.
-- ifnull(값,0) : 값이 null이면 0으로 리턴
select ename, sal, comm, sal + ifnull(comm,0) as "지급액" from emp;



