[README.txt]

# 터미널창에서 프로그램 실행
fastapi dev

# 프로그램을 실행하면 자동으로 테이블(todo)을 생성
CREATE TABLE todo (
        id INTEGER NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        is_done BOOL NOT NULL,
        PRIMARY KEY (id)
)

# 테스트 코드
# 다음과 같이 미리 테이블을 생성하고 데이터를 입력
DROP TABLE IF EXISTS todo;
CREATE TABLE todo (
        id INTEGER NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        is_done BOOL NOT NULL,
        PRIMARY KEY (id)
);

INSERT INTO todo (title, is_done) VALUES
	('청소하기', false),
   	('공부하기', false),
   	('영화보기', false);
COMMIT;

SELECT * FROM todo;

