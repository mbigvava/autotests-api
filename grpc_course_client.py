import grpc

import course_service_pb2
import course_service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = course_service_pb2_grpc.CourseServiceStub(channel)

        request = course_service_pb2.GetCourseRequest(course_id="api-course")

        # Вызываем метод GetCourse
        response = stub.GetCourse(request)

        # Выводим ответ
        print(response)

if __name__ == '__main__':
    run()