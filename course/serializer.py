from rest_framework import serializers
from course.models import Course, Lesson, Countlesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.IntegerField(source='countlesson.count_lesson', read_only=True)

    lessons = LessonSerializer(many=True)  # Сериализатор для представления уроков

    """Добавление поля для вывода количества уроков
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        # Метод для подсчета количества уроков
        return obj.lessons.count()"""


    class Meta:
        model = Course
        fields = ('title_course', 'preview_course', 'description_course', 'count_lesson', 'lessons')

class CountlessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countlesson
        fields = '__all__'



