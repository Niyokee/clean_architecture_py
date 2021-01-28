# Repositoryは Interface Adapterレイヤーにあるgatewayパターン
# DBとusecaseとentityのアダプタ

from domain.domain.user import User
from abc import ABCMeta, abstractmethod

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_user_name(self, user_name: str):
        pass

    @abstractmethod
    def save(self, user: User):
        pass