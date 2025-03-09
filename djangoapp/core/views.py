from django.shortcuts import render
from rest_framework import viewsets
from users.models import Client, Farm, Transaction
from .serializers import ClientSerializer, FarmSerializer, TransactionSerializer


def initial(request):
    return render(request, "initial.html")     

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
