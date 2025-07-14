from api_client_create_course import courses_client
from clients.courses.courses_client import CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercise_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
exercises_client = get_exercise_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="exercise",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file_api(create_file_request)
print('Create file data:', create_file_response.json())

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.json()['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course_api(create_course_request)
print('Create course data:', create_course_response.json())

# Создаем упражнения
create_exercises_request = CreateExerciseRequestDict(
    title="Exercise 1",
    courseId = create_course_response.json()['course']['id'] ,
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)
create_exercise_response = exercises_client.create_exercise_api(create_exercises_request)
print('Create exercise data:', create_exercise_response.json())

