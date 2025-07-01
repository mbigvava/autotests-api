import httpx

login_payload = {
  "email": "mbigvava@at-consulting.ru",
  "password": "Qwerty12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data =login_response.json()

print(login_response.json())
print(login_response.status_code)

# в headers + дописывает строку
headers = {"Authorization": "Bearer "+login_response_data['token']['accessToken']}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(response.status_code)
print(response.json())
#вытащить через print рефреш используя get response
print(login_response_data['token']['refreshToken'])
print("test")