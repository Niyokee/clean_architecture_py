from abc import ABCMeta, abstractmethod
from user.user_create_input_data import UserCreateInputData


class IUserCreateUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, input_data: UserCreateInputData):
        pass