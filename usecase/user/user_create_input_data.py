from user.i_user_create_use_case import IUserCreateUseCase

# インターフェースを実装したクラス
# DTO: 異なるレイヤーでデータを受け渡すのに使用する
class UserCreateInputData(IUserCreateUseCase):
    def __init__(self, user_name: str):
        self.user_name = user_name
