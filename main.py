from mixin import *

class User(LoginMixin, RegisterMixin, ChangePasswordMixin, ChangeUsernameMixin):
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = password

    def login(self):
        return super().login(self.name, self.password)

    def register(self):
        return super().register(self.name, self.password)

    def change_password(self, new_password:str):
        return super().change_password(self.name, self.password, new_password)

    def change_name(self ,new_name: str):
        return super().change_name(self.name, new_name)

    def __str__(self) -> str:
        return self.name


class Post(CheckOwnerMixin):
    def __init__(self,title: str, description: str, price: int, quantity: int, owner: str) -> None:
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = self.check(owner)

    def __str__(self) -> str:
        return self.title




