from entity.domain.user.user import User
from entity.domain.user.user_repository import IUserRepository


class InMemoryUserRepository(IUserRepository):

    def __init__(self):
        self.data = {}

    def save(self, user: User):
        self.data[user.id] = self.clone_user(user)

    def find_by_user_name(self, user_name: str):
        key = [k for k, v in self.data.items() if v.name == user_name]
        return self.data[key]

    def clone_user(self, user: User):
        return User(user.id, user.name)
