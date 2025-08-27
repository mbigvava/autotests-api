# Генерация фейковых данных
# Faker предоставляет множество методов для генерации данных. Вот некоторые из них:
#
# Имя: fake.name() — генерирует случайное имя.
# Адрес: fake.address() — генерирует фейковый адрес.
# Электронная почта: fake.email() — генерирует фейковый email.
# Телефон: fake.phone_number() — генерирует фейковый номер телефона.
# Компания: fake.company() — генерирует название компании.

fake = Faker('ru_RU')
print(fake.name())         # Выведет: Иван Иванов
print(fake.address())      # Выведет: ул. Пушкина, дом 10

from faker import Faker
import requests

fake = Faker()

# Генерация фейковых данных
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

# Отправка POST-запроса с фейковыми данными
response = requests.post("https://api.example.com/users", json=user_data)

# Проверка, что запрос прошел успешно
assert response.status_code == 201