-- 데이터 사전(Data Dictionary) : MySQL에서는 information_schema를 활용합니다.

-- information_schema.TABLES 테이블 구조 확인
DESC information_schema.TABLES;
-- TABLE_NAME       VARCHAR(64)   테이블 명
-- TABLE_COMMENT    VARCHAR(2048) 설명

-- 테이블 딕셔너리 정보 조회 
SELECT table_name, table_comment FROM information_schema.TABLES WHERE table_schema = 'information_schema' AND table_name LIKE 'USER_%' ORDER BY 1;

-- 접속한 데이터베이스(스키마)가 소유한 객체 정보
SELECT * FROM information_schema.TABLES WHERE table_schema = DATABASE();
SHOW TABLES;

-- 모든 테이블 정보
SELECT * FROM information_schema.TABLES;

-- OWNER (SCHEMA) : scott
SELECT * FROM information_schema.TABLES WHERE table_schema = 'scott';

-- 시스템 전체 테이블 정보 (관리자 권한)
SELECT * FROM information_schema.TABLES;
DESC information_schema.TABLES;


