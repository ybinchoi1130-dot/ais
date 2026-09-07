use aisdb;

-- 테이블 삭제
DROP TABLE IF EXISTS items;

-- 테이블 생성
CREATE TABLE items (
    item_id INTEGER PRIMARY KEY AUTO_INCREMENT, -- 메인키, 자동번호생성
    name TEXT,       -- 아이템 이름
    price INTEGER    -- 가격
);


INSERT INTO items (name, price)	VALUES ('수박', 26000);
    
INSERT INTO items (name, price) VALUES
	('오이', 700),
	('마늘', 1000),
    ('양파', 4500);

COMMIT;
    
select * from items;
