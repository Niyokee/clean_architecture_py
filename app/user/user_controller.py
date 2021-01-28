# Controllerはユーザーの入力をusecaseに伝える

from domain.application.user.user_create_interactor import UserCreateInteractor
from usecase.user.i_user_create_use_case import IUserCreateUseCase
from usecase.user.user_create_input_data import UserCreateInputData

class UserController:

    def __init__(self, user_create_use_case: IUserCreateUseCase):
        self.user_create_use_case = user_create_use_case

    def create_user(self, user_name):
        input_data = UserCreateInputData(user_name)
        self.user_create_use_case.handle(input_data)