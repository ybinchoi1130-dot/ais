
-- 사용자 계정 삭제
DROP USER IF EXISTS 'school'@'localhost';
FLUSH privileges;

-- 외부 접속 계정 삭제
-- DROP USER IF EXISTS 'school'@'%';

-- 사용자 생성
-- 사용자 계정: school
-- 사용자 비번: school
-- 로컬 접속 허용 계정
CREATE USER 'school'@'localhost' IDENTIFIED BY 'school';

-- 외부 접속 허용 계정
-- CREATE USER 'school'@'%' IDENTIFIED BY 'school';

-- 권한 부여
-- 데이터베이스의 모든 권한: school.*
-- 사용자 계정: school
GRANT ALL PRIVILEGES ON school.* TO 'school'@'localhost';

-- 변경된 권한을 즉각 반영하라.
FLUSH PRIVILEGES;