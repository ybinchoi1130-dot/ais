
-- 사용자 계정 삭제
DROP USER IF EXISTS 'scott'@'localhost';
FLUSH privileges;

-- 외부 접속 계정 삭제
-- DROP USER IF EXISTS 'scott'@'%';

-- 사용자 생성
-- 사용자 계정: scott
-- 사용자 비번: scott
-- 로컬 접속 허용 계정
CREATE USER 'scott'@'localhost' IDENTIFIED BY 'scott';

-- 외부 접속 허용 계정
-- CREATE USER 'scott'@'%' IDENTIFIED BY 'scott';

-- 권한 부여
-- 데이터베이스의 모든 권한: scott.*
-- 사용자 계정: scott
GRANT ALL PRIVILEGES ON scott.* TO 'scott'@'localhost';

-- 변경된 권한을 즉각 반영하라.
FLUSH PRIVILEGES;