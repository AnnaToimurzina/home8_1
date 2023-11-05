from django.urls import path
from rest_framework.routers import DefaultRouter

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionCreateView, SubscriptionDestroyAPIView, SubscriptionViewSet

app_name = SubscriptionConfig.name

router = DefaultRouter()
router.register(r'subscription', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('subscriptions/<int:course_id>/', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('subscriptions/<int:course_id>/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'),
]