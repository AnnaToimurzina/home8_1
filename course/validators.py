import re

from rest_framework.exceptions import ValidationError


class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        '''валидатор проверяет, соответствует ли переданное значение ссылке на youtube.com'''
        youtube_pattern = re.compile(r'^https?://(www\.)?youtube\.com/.+')
        youtube_val = dict(value).get(self.field)
        if not bool(youtube_pattern.match(youtube_val)):
            raise ValidationError("Ссылки на сторонние ресурсы, кроме youtube.com, не разрешены.")

