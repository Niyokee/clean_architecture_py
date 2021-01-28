from datetime import date
from domain.domain.user.user import User
from domain.domain.user.user_repository import IUserRepository
from usecase.user.i_user_create_use_case import IUserCreateUseCase
from usecase.user.user_create_input_data import UserCreateInputData
from usecase.user.user_create_output_data import UserCreateOutputData

# use_caseの実装→ Interactor
class UserCreateInteractor(IUserCreateUseCase):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def handle(self, input_data: UserCreateInputData):
        user_name = input_data.user_name
        duplicate_user = self.user_repository.find_by_user_name(user_name)
        if duplicate_user is not None:
            raise ValueError

        user = User(user_name)
        self.user_repository.save()

        output_data = UserCreateOutputData(user.id, date())
        # presentere.complete
