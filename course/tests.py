from django.test import TestCase
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


class CourseTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.data = {
            'title_course': 'New Course',
            'preview_course': 'Course Preview',
            'description_course': 'Course Description'
        }
        self.url = '/path-to-your-course-create-view/'

    def test_create_course(self):
        client = APIClient()
        client.login(username='testuser', password='testpassword')
        response = client.post('/api/courses/', self.course_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_course(self):
        client = APIClient()
        response = client.get('courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_course(self):
        client = APIClient()
        client.login(username='testuser', password='testpassword')
        updated_data = {'title_course': 'Updated Course Title'}
        response = client.put(f'/api/courses/{self.course.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_course(self):
        client = APIClient()
        client.login(username='testuser', password='testpassword')
        response = client.delete(f'/api/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    class LessonTests(TestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='testpassword')
            self.course = Course.objects.create(title_course='Test Course', preview_course='Course Preview',
                                                description_course='Course Description')
            self.lesson_data = {'content': 'Lesson Content', 'course': self.course}
            self.lesson = Lesson.objects.create(**self.lesson_data)

        def test_create_lesson(self):
            client = APIClient()
            client.login(username='testuser', password='testpassword')
            response = client.post('/api/lessons/', self.lesson_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_read_lesson(self):
            client = APIClient()
            response = client.get('/api/lessons/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_update_lesson(self):
            client = APIClient()
            client.login(username='testuser', password='testpassword')
            updated_data = {'content': 'Updated Lesson Content'}
            response = client.put(f'/api/lessons/{self.lesson.id}/', updated_data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_delete_lesson(self):
            client = APIClient()
            client.login(username='testuser', password='testpassword')
            response = client.delete(f'/api/lessons/{self.lesson.id}/')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

