from datetime import date

class UserCreateOutputData:
    """ユーザー登録後に必要な情報を定義
       DTO: 異なるレイヤーでデータを受け渡すのに使用する
    """

    def __init__(self, user_id: str, created: date):
        self.user_id = user_id
        self.created = created

