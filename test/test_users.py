from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
# Импортируем функцию проверки статус-кода
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response

def test_create_user():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()

    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema()
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)
    # Инициализируем модель ответа на основе полученного JSON в ответе
    # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # Используем функцию для проверки статус-кода
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())


    #Запуск python -m pytest -k "test_create_user" -s -v
    #-m pytest — запуск тестов с помощью pytest.
    # -k "test_create_user" — фильтрация тестов, чтобы запустить только test_create_user.
    # -s — позволяет выводить в консоль print() и stdout(если есть в тестах).
    # -v — включает подробный вывод (verbose).