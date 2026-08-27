-- 날짜 함수 
-- datetime
-- date_format()
-- year()
-- month()
-- day()

desc emp;
-- 결과: 월이나 일이 1자리인 경우 '0'이 앞에 붙음
select hiredate,
	date_format(hiredate,'%Y%m%d') as '날짜', -- 문자열로 변환 됨
    substr(date_format(hiredate,'%Y%m%d'),1,4) as '연도',
    substr(date_format(hiredate,'%Y%m%d'),5,2) as '월',
    substr(date_format(hiredate,'%Y%m%d'),7,2) as '일' from emp;
    
    
select hiredate,
    year(hiredate) as '연도',
    month(hiredate) as '월',
    day(hiredate) as '일' from emp;