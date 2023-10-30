from django.urls import path
from rest_framework.routers import DefaultRouter

from payments.apps import PaymentsConfig
from payments.views import PaymentsViewSet, PaymentsCreateView, PaymentsListView

app_name = PaymentsConfig.name

router = DefaultRouter()
router.register(r'payment', PaymentsViewSet, basename='payment')

urlpatterns = [path('payment/create', PaymentsCreateView.as_view(), name='payment_create'),
        path('payment/list', PaymentsListView.as_view(), name='payment_list'),


               ] + router.urls