#Создаём класс AuthenticationClient
from clients.api_client import APIClient


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    pass

# Реализуем метод login_api
from httpx import Response

from clients.api_client import APIClient


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: dict) -> Response:
        # request: dict — тело запроса в JSON - формате.
        # self.post(...) — метод APIClient, который делает POST - запрос.
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

# Используем TypedDict для аннотации параметров. TypedDict из typing позволяет создавать строгие типизированные словари,
# указывая обязательные поля
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    # Реализуем метод refresh_api
    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)