# Generated by Django 4.2.6 on 2023-10-29 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(to='course.lesson', verbose_name='Связь курс-уроки'),
        ),
    ]
