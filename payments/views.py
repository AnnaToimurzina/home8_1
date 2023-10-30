from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

import payments
from payments.models import Payment
from payments.serializer import PaymentSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class PaymentsCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

class PaymentsListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = payments
    ordering_fields = ('payment_date', 'user', 'course', 'lesson', 'payment_method')
