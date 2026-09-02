-- aisdb

-- 데이터베이스 삭제
DROP DATABASE IF EXISTS aisdb;

-- 데이터베이스 생성: aisdb
-- COLLATE utf8_general_ci: ci(Case Insensitive)
-- Case Insensitive: 
--  문자열 데이터 타입(VARCHAR, CHAR)
--  데이터베이스 엔진이 값을 비교할 때 대소문자를 같은 문자로 취급  
CREATE DATABASE aisdb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

SHOW databases;

USE aisdb;


-- 사용자 계정 삭제
DROP USER IF EXISTS 'aisdb'@'localhost';
FLUSH privileges;

-- 외부 접속 계정 삭제
-- DROP USER IF EXISTS 'aisdb'@'%';

-- 사용자 생성
-- 사용자 계정: aisdb
-- 사용자 비번: aisdb
-- 로컬 접속 허용 계정
CREATE USER 'aisdb'@'localhost' IDENTIFIED BY 'aisdb';

-- 외부 접속 허용 계정
-- CREATE USER 'aisdb'@'%' IDENTIFIED BY 'aisdb';

-- 권한 부여
-- 데이터베이스의 모든 권한: aisdb.*
-- 사용자 계정: aisdb
GRANT ALL PRIVILEGES ON aisdb.* TO 'aisdb'@'localhost';

-- 변경된 권한을 즉각 반영하라.
FLUSH PRIVILEGES;