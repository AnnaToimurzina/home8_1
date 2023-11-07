from django.conf import settings
from django.db import models

from Users.models import User


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=100, verbose_name='Название урока')
    description_lesson = models.TextField(verbose_name='Описание урока')
    preview_lesson = models.ImageField(upload_to='lesson_previews/', null=True, blank=True,
                                       verbose_name='Картинка курса')
    video_link = models.URLField(verbose_name='Ссылка на урок')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description_lesson, self.description_lesson, self.preview_lesson, self.video_link

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Course(models.Model):
    title_course = models.CharField(max_length=100, verbose_name='Название курса')
    preview_course = models.ImageField(upload_to='course_previews/', null=True, blank=True, verbose_name='Картинка')
    description_course = models.TextField(verbose_name='Описание')
    lessons = models.ManyToManyField(Lesson, verbose_name='Связь курс-уроки', related_name='courses')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title_course, self.preview_course, self.description_course, self.lessons

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'




class Countlesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True, blank=True)
    count_lesson = models.PositiveIntegerField(verbose_name='Количество уроков')


    def __str__(self):
        return self.course, self.count_lesson

    class Meta:
        verbose_name = 'количество уроков'
        verbose_name_plural = 'Количество уроков'




