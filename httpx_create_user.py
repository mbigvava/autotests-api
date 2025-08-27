#user creation
import httpx
#генерация случайно email
from tools.fakers import fake
payload = {
    "email": fake.email(),
    "password": "<PASSWORD>",
    "lastName": "Test1",
    "password": "Qwerty12345",
    "lastName": "Test",
    "firstName": "Mariam",
    "middleName": "Testovich"
}
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
private_users_client = get_private_users_client(authentication_user)

# Используем метод get_user
get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print('Get user data:', get_user_response)
