select * from todo;
select * from user;
insert into user (email, hashed_password) values ('abc@abc.com', 'abc');

insert into todo (title, is_done) values ('여행하기', false);
insert into todo (title, is_done) values ('쇼핑하기', false);
insert into todo (title, is_done, user_id) values ('학습하기', false, 1);
commit;

select u.id, u.email, t.title, t.user_id
    FROM user u join todo t on u.id = t.user_id;

