import os
import psycopg2 as pg
from sqlalchemy import create_engine

bool_t = bool  # Need alias because NDFrame has def bool:


class DB:

    def __init__(self, target: str):
        """DBクラスの初期化メソッド

        Args:
            target (str): 接続するdbを指定する
        """
        self.set_target(target)

    def set_target(self, target: str):
        """接続するDBの情報をsetするメソッド

        Args:
            target (str): 接続先のdbを指定する

        Raises:
            AttributeError: rails or public以外のdbを指定するとエラーになる
        """
        if target == 'rails':
            self.prefix: str = 'DATABASE_'
        elif target == 'public':
            self.prefix: str = 'POSTGIS_'
        else:
            raise ValueError('targetは rails か publicのいづれかを指定してください')

    def connect(self):
        """DBの接続情報をインスタンス変数に格納する
        """
        conn = pg.connect(
            user=os.environ[self.prefix + "USERNAME"],
            host=os.environ[self.prefix + "HOST"],
            password=os.environ[self.prefix + "PASSWORD"],
            port=os.environ[self.prefix + "PORT"],
            dbname=os.environ[self.prefix + "NAME"]
        )
        conn.set_client_encoding('utf-8')
        return conn

    def engine(self):
        """DBの接続情報をインスタンス変数に格納する
        """
        self.engine_ = create_engine(
            "postgresql://" +
            os.environ[self.prefix + "USERNAME"] +
            ":" +
            os.environ[self.prefix + "PASSWORD"] +
            "@" +
            os.environ[self.prefix + "HOST"] +
            ":" +
            os.environ[self.prefix + "PORT"] +
            "/" +
            os.environ[self.prefix + "NAME"], use_batch_mode=True)
