#Добавляем авторизационные заголовки на уровне клиента
import httpx

# Проходим аутентификацию
login_payload = {
    "email": "mbigvava@at-consulting.ru",
    "password": "Qwerty12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Инициализируем клиент с base_url и timeout
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