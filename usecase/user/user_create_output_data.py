from datetime import date

# DTO: 異なるレイヤーでデータを受け渡すのに使用する
class UserCreateOutputData:

    def __init__(self, user_id: str, created: date):
        self.user_id = user_id
        self.created = created

