import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if not re.match("^[a-z]{3,}$", username):
            raise AuthenticationError("The username must consist of the letters a-z and its length must be at least 3")
        if len(password) < 8 or re.match("^[a-Ö]{8,}$", password):
            raise AuthenticationError("The password must be at least 8 characters long and contain 1 or more characters other than a-ö")
