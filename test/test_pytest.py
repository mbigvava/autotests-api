def test_user_login():
    assert 1 == 1

class TestUserAuthentication:
    def test_login(self):
        assert 1 == 1

#запуск командой python -m pytest
#Примеры правильного именования классов:  TestProfile /TestCourses/ TestUserAuthorization

def test_first_try():
    print("Hello World!")

"""
Чтобы в  лог выводилось больше информации, включая содержимое консольных сообщений, 
необходимо добавить флаг - s. Этот  флаг позволяет отображать вывод функций print().

python -m pytest -v -s

Pytest также поддерживает запуск тестов, имена которых частично совпадают с указанным шаблоном. 
Для этого можно использовать опцию -k, которая позволяет фильтровать тесты по имени.

python -m pytest -k "login"

Запуск всех тестов, где имя функции содержит "login" и "success":

python -m pytest -k "login and success"
            
Запуск всех тестов, где имя содержит "login", но исключает "failed":

python -m pytest -k "login and not failed"

"""
def test_greeting():
    greeting = "Hello, world!"
    assert greeting == "Hi, world!"

#Основные типы проверок:
    # Равенство:
def test_equal():
    assert 1 == 1
#Неравенство:
def test_not_equal():
    assert 1 != 2
#Проверка вхождения элемента:
def test_in_list():
    assert 3 in [1, 2, 3, 4]

#Проверка булевого значения:
def test_boolean():
    is_authenticated = True
    assert is_authenticated

#Если булевое значение True, тест пройдет.Если False — тест упадет.

 #Проверка исключений: pytest имеет встроенные средства для проверки того, что в коде выбрасывается нужное исключение.
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_sum():
    assert 1 + 1 == 3, "Сумма 1 и 1 должна быть 2!"

def test_first_try():  # Этот тест мы добавили в предыдущем шаге
    print("Hello World!")


def test_assert_positive_case():  # Новый тест, которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 2) == 5  # Тут должна быть ошибка

#запустим автотесты командой: python -m pytest -k "test_assert_" -s -v