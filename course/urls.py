from django.urls import path
from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import CourseViewSet, LessonCreateView, LessonListView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
        path('lesson/', LessonCreateView.as_view(), name='lesson-list-create'),
        path('lesson/list', LessonListView.as_view(), name='lesson-list'),
        path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
        path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
        path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete')
               ] + router.urls