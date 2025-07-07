#Реализуем базовый API клиент
from typing import Any
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles

class APIClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        return self.client.delete(url)


# #Реализуем метод GET
#
#     from httpx import Client, URL, Response, QueryParams
#
#     class APIClient:
#         def __init__(self, client: Client):
#             self.client = client
#
#         def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
#             """
#             Выполняет GET-запрос.
#
#             :param url: URL-адрес эндпоинта.
#             :param params: GET-параметры запроса (например, ?key=value).
#             :return: Объект Response с данными ответа.
#             """
#             return self.client.get(url, params=params)
# # Метод get принимает URL и параметры запроса (params).
# # params — это словарь или кортежи ключ-значение, передаваемые в строке запроса (query string), например: ?name=John&age=30.
# # Метод возвращает объект Response, содержащий ответ от сервера.
#
# # Реализуем метод POST
#
#     def post(
#             self,
#             url: URL | str,
#             json: Any | None = None,
#             data: RequestData | None = None,
#             files: RequestFiles | None = None
#     ) -> Response:
#         """
#         Выполняет POST-запрос.
#
#         :param url: URL-адрес эндпоинта.
#         :param json: Данные в формате JSON.
#         :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
#         :param files: Файлы для загрузки на сервер.
#         :return: Объект Response с данными ответа.
#         """
#         return self.client.post(url, json=json, data=data, files=files)
#
# # Разбор кода:
# # Добавлены параметры data и files, которые понадобятся в будущем, например, для загрузки файлов через эндпоинт /api/v1/files.
# # json используется для передачи данных в формате JSON.
# # data передает параметры в x-www-form-urlencoded формате.
# # files позволяет загружать файлы на сервер.
#
# # Реализуем метод patch, delete
#
#     def patch(self, url: URL | str, json: Any | None = None) -> Response:
#         """
#         Выполняет PATCH-запрос (частичное обновление данных).
#
#         :param url: URL-адрес эндпоинта.
#         :param json: Данные для обновления в формате JSON.
#         :return: Объект Response с данными ответа.
#         """
#         return self.client.patch(url, json=json)
#
#     def delete(self, url: URL | str) -> Response:
#         """
#         Выполняет DELETE-запрос (удаление данных).
#
#         :param url: URL-адрес эндпоинта.
#         :return: Объект Response с данными ответа.
#         """
#         return self.client.delete(url)
#
# # Разбор кода:
# # patch используется для частичного обновления ресурса, передавая измененные данные.
# # delete удаляет ресурс по указанному URL.
# В обоих методах в Response возвращается объект ответа сервера.