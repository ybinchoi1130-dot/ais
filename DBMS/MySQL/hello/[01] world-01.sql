-- Ctrl+Shift+Enter: 현재 파일의 모든 내용을 시행
-- Ctrl+Enter: 현재 커서가 있는 위치의 명령을 실행

-- 스키마 선택
use world;

-- 테이블 목록 조회
show tables;

-- Table('city')의 모든 컬럼의 내용을 조회
-- 조회: SELECT
-- 컬럼: *(모든 컬럼)
-- 테이블: FROM 테이블명
SELECT * FROM city;

SELECT * FROM country;

SELECT * FROM countrylanguage;