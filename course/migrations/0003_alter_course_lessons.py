# Generated by Django 4.2.6 on 2023-10-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(related_name='courses', to='course.lesson', verbose_name='Связь курс-уроки'),
        ),
    ]
