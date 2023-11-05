from rest_framework import serializers
from course.models import Course, Lesson, Countlesson
from course.validators import TitleValidator
from subscription.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.IntegerField(source='countlesson.count_lesson', read_only=True)

    lessons = LessonSerializer(many=True)  # Сериализатор для представления уроков

    is_subscribed = serializers.SerializerMethodField() #информация о подписке текущего пользователя на курс

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscription.objects.filter(user=user, course=obj).exists()
        return False


    class Meta:
        model = Course
        fields = ('title_course', 'preview_course', 'description_course', 'count_lesson', 'lessons', 'is_subscribed')
        validators = [TitleValidator(field='video_link')]

class CountlessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countlesson
        fields = '__all__'



