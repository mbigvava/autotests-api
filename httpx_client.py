import httpx

# Инициализируем клиент - создаёт экземпляр клиента httpx.Client, который позволяет
# управлять HTTP-соединениями и повторно использовать TCP-соединение между запросами.
client = httpx.Client()

# Выполняем GET-запрос, используя клиент
response = client.get("http://localhost:8000/api/v1/users/me")

# Выводим ответ в консоль
print(response.text)

#Используем base_url для упрощения кода - заменяем шаблонный код
import httpx

# Инициализируем клиент с base_url  – теперь все запросы будут автоматически дополняться этим базовым URL
client = httpx.Client(base_url="http://localhost:8000")

# Выполняем GET-запрос, используя относительный путь – вместо полного URL передаём только путь.
response = client.get("/api/v1/users/me")

# Выводим ответ в консоль
print(response.text)

#Добавляем timeout для всех запросов
import httpx

# Инициализируем клиент с base_url и timeout
client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100  # Таймаут в секундах – теперь все запросы автоматически используют этот таймаут.
)

# Выполняем GET-запрос
response = client.get("/api/v1/users/me")
print(response.text)

#Добавляем авторизационные заголовки на уровне клиента
import httpx

# Проходим аутентификацию
login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Инициализируем клиент с авторизацией
client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

# Выполняем запрос с авторизацией
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print('Get user me data:', get_user_me_response_data)

# Мы выполняем POST-запрос для получения accessToken.
# Используем headers={"Authorization": f"Bearer {token}"} при создании клиента.
# Теперь все запросы автоматически включают этот заголовок.