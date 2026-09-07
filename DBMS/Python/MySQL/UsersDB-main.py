# -*- coding: utf-8 -*-

from UsersDB import UsersDB

if __name__ == "__main__":
    db = UsersDB()

    db.delete_users_all()

    db.insert_users('이순신', 45, 'lss@abc.com', '12345', '충청도 서산')
    db.insert_users('유관순', 20, 'rgs@abc.com', '12345', '경기도 천안')
    db.insert_users('강감찬', 53, 'ggc@abc.com', '12345', '평안도 평양')

    db.delete_users('홍길동')
    db.delete_users('전우치')

    db.update_users('강감찬', 64, 'ggc@abc.com', '54321', '평안도 개성')
    db.select_users()
    db.close()



