from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    city = models.CharField(max_length=100, verbose_name='City')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar')

    def __str__(self):
        return self.email, self.phone, self.city, self.avatar

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Course(models.Model):
    title_course = models.CharField(max_length=100, verbose_name='Название курса')
    preview_course = models.ImageField(upload_to='course_previews/', null=True, blank=True, verbose_name='Картинка')
    description_course = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title_course, self.preview_course, self.description_course

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=100, verbose_name='Название урока')
    description_lesson = models.TextField(verbose_name='Описание урока')
    preview_lesson = models.ImageField(upload_to='lesson_previews/', null=True, blank=True, verbose_name='Картинка курса')
    video_link = models.URLField(verbose_name='Ссылка на урок')

    def __str__(self):
        return self.description_lesson, self.description_lesson, self.preview_lesson, self.video_link

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'