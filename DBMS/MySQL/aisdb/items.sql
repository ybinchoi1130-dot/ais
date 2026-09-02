use aisdb;
select * from items;

INSERT INTO items (name, price)	VALUES ('수박', 26000);
    
INSERT INTO items (name, price) VALUES
	('오이', 700),
	('마늘', 1000),
    ('양파', 4500);

COMMIT;
    
select * from items;
