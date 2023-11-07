from rest_framework import generics, viewsets, serializers
from rest_framework.permissions import AllowAny

from course.models import Lesson, Course, Countlesson
from course.paginator import MyPagination
from course.permissions import IsModeratorReadOnly
from course.serializer import LessonSerializer, CourseSerializer, CountlessonSerializer



class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MyPagination


class CourseCreateView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsModeratorReadOnly]

class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModeratorReadOnly]

class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

class LessonListView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MyPagination

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModeratorReadOnly]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]

class CountlessonCreateView(generics.CreateAPIView):
    serializer_class = CountlessonSerializer

class CountlessonlistView(generics.ListAPIView):
    serializer_class = CountlessonSerializer
    queryset = Countlesson.objects.all()