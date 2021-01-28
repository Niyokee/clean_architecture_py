import psycopg2 as pg

from domain.user.user import User
from postgis_infra.postgis import DB

from domain.user.user import User
from domain.user.user_repository import IUserRepository

class UserRepository(IUserRepository):

    def find_by_user_name(self, user_name: str):
        sql = 'SELECT * FROM users where name == %s'
        db = DB('rails')
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_name))
        return cur.fetchall()


    def save(self, user: User):
        params = (user.id, user.name)
        sql = 'INSERT INTO users (id, name) VALUES (%i, %s)'
        db = DB('rails')
        with db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, params)
            conn.commit()


