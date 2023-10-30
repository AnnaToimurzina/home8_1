from rest_framework import generics, viewsets

from course.models import Lesson, Course, Countlesson
from course.serializer import LessonSerializer, CourseSerializer, CountlessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

class CountlessonCreateView(generics.CreateAPIView):
    serializer_class = CountlessonSerializer

class CountlessonlistView(generics.ListAPIView):
    serializer_class = CountlessonSerializer
    queryset = Countlesson.objects.all()