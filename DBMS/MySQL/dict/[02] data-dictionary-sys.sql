-- OWNER (SCHEMA) : scott
SELECT * FROM information_schema.TABLES WHERE table_schema = 'scott';

-- 시스템(DBA) 권한 테이블
SELECT * FROM information_schema.TABLES;
DESC information_schema.TABLES;

-- 사용자 정보 (MySQL에서는 mysql.user 테이블을 사용합니다)
-- SELECT * FROM dict WHERE table_name = 'DBA_USERS';
DESC mysql.user;
SELECT * FROM mysql.user;
SELECT * FROM mysql.user WHERE user = 'scott';

-- 제약조건 검색 (MySQL에서는 information_schema.TABLE_CONSTRAINTS 사용)
DESC information_schema.TABLE_CONSTRAINTS;
SELECT * FROM information_schema.TABLE_CONSTRAINTS;
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE constraint_schema = 'scott';
SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE table_name = 'EMP';
