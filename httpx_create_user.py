#user creation
import httpx
#генерация случайно email
#from tools.fakers import get_random_email и тогда в "email": get_random_email(),
payload = {
    "email": "user1@gmail.com",
    "password": "Qwerty12345",
    "lastName": "Test",
    "firstName": "Mariam",
    "middleName": "Testovich"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())

#запуск скрипта python -m httpx_create_user