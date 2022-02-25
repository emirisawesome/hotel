from rest_framework.routers import DefaultRouter
from django.urls import path,include,re_path
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('menu', RoomView)
router.register('room', MenuView)
router.register('order',OrderView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]