"""С паттерном Facade все API вызовы инкапсулируются в один класс:"""
class UsersClient:
    def __init__(self, base_url: str):
        self.client = httpx.Client(base_url=base_url)

    def get_user(self, user_id: str):
        return self.client.get(f"/api/v1/users/{user_id}")

    def update_user(self, user_id: str, data: dict):
        return self.client.patch(f"/api/v1/users/{user_id}", json=data)

    def delete_user(self, user_id: str):
        return self.client.delete(f"/api/v1/users/{user_id}")

"""Теперь клиентский код выглядит чисто и понятно:"""

    client = UsersClient(base_url="https://example.com")

    response = client.get_user(user_id)
    response = client.update_user(user_id, {"email": "new@example.com"})
    response = client.delete_user(user_id)

""""Паттерн Facade делает код структурированным, читабельным и удобным в использовании."""