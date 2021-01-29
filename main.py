from injector import Injector, Module
from entity.domain.user.user_repository import IUserRepository
from infra.database.user.user_repository import UserRepository
from entity.application.user.user_create_interactor import UserCreateInteractor
from usecase.user.create.i_user_create_use_case import IUserCreateUseCase
from infra.controllers.user_controller import UserController


class UserControllerDIModule(Module):
    def configure(self, binder) -> None:
        binder.bind(IUserCreateUseCase, to=UserCreateInteractor)


class UserCreateInteractorDIModule(Module):
    def configure(self, binder) -> None:
        binder.bind(IUserRepository, to=UserRepository)


if __name__ == '__main__':
    injector = Injector([UserControllerDIModule(), UserCreateInteractorDIModule()])
    controller = injector.get(UserController)
    controller.create_user('user_name')
