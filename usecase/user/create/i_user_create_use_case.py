from abc import ABCMeta, abstractmethod
from usecase.user.create.user_create_input_data import UserCreateInputData

class IUserCreateUseCase(metaclass=ABCMeta):
    """ユーザー登録のインターフェース
    　　ユーザーを登録するために必要な引数を定義
    """
    @abstractmethod
    def handle(self, input_data: UserCreateInputData):
        pass