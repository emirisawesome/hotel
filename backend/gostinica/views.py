from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RoomSerializer,MenuSerializer,OrderSerializer
from .models import Room,Menu,Order

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    def get_queryset(self):
        return self.queryset
class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    def get_queryset(self):
        return self.queryset

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    def get_queryset(self):
        return self.queryset

