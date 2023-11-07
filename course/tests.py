from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework_simplejwt.tokens import AccessToken

from .models import Lesson, Course
from Users.models import User

class LessonCRUDTest(TestCase):
    def setUp(self):

        self.user = User.objects.create(email='test_anna@test.ru') # Создаем пользователя
        self.user.set_password('test')
        self.user.save()



        self.course = Course.objects.create(
            title_course='Test',
            description_course='Test description',
            user=self.user)


        self.lesson = Lesson.objects.create(
            title_lesson='TestLesson',
            description_lesson='Test lesson description',
            video_link='https://www.youtube.com/',
            user=self.user)

        self.course.lessons.add(self.lesson)

    def test_lesson_create(self):
        url = reverse('course:lesson_create')
        data = {
            'title_lesson': 'TestLesson1',
            'description_lesson': 'Test lesson description1',
            'video_url': 'https://www.youtube.com/',
            "course": self.course.id,
            "user": self.user.id
        }

        response = self.client.post(url, data=data)
        print(response.json())

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Lesson.objects.all().exists(),
            {
                'id': 2,
                'title_lesson': 'TestLesson2',
                'description_lesson': 'Test lesson description2',
                'video_url': 'https://www.youtube.com',
                "course": 2,
                "user": 2

            }
        )

    def test_lesson_list(self):
        url = reverse('course:lesson_list')

        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json().get('results'),
            [
                {
                    "id": self.lesson.pk,
                    "title_lesson": self.lesson.title_lesson,
                    "description_lesson": self.lesson.description_lesson,
                    "video_link": self.lesson.video_link,
                    "preview_lesson": self.lesson.preview_lesson,
                    "user": self.user.pk,

                }
            ]
        )

    def test_lesson_detail(self):
        url = reverse('course:lesson-get', kwargs={'pk': self.lesson.pk})

        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {
                "id": self.lesson.pk,
                "title_lesson": self.lesson.title_lesson,
                "description_lesson": self.lesson.description_lesson,
                "video_link": self.lesson.video_link,
                "preview_lesson": self.lesson.preview_lesson,
                "user": self.user.pk,

            }
        )

    def test_lesson_delete(self):
        url = reverse('course:lesson-delete', kwargs={'pk': self.lesson.pk})

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Lesson.objects.all().exists(),
        )




