from django.contrib import admin
from .models import Lesson, Course

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title_lesson', 'description_lesson', 'preview_lesson', 'video_link')
    list_filter = ('title_lesson',)
    search_fields = ('title_lesson', 'description_lesson', 'preview_lesson')


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title_course', 'description_course', 'preview_course')
    list_filter = ('title_course',)
    search_fields = ('title_course', 'description_course', 'preview_course')