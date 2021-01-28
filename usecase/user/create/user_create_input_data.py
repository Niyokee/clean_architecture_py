from user.create.i_user_create_use_case import IUserCreateUseCase

class UserCreateInputData():
    """IUserCreateUseCaseを実装したクラス
    　　Userを作成するために必要な引数をとる。
        DTO: 異なるレイヤーでデータを受け渡すのに使用する
    """
    def __init__(self, user_name: str) -> None:
        self.user_name = user_name
