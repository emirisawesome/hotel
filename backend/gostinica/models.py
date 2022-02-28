from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    descriptions = models.CharField(max_length=1200)


s = (
    ("ekonomy", "ekonomy"),
    ("standart", "standart"),
    ("lux", "lux"),
    ("penthaus", "penthaus"),
    ("prezident", "prezident"),
)

times = (
    ((datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"), "1"),
    ((datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%Y-%m-%d"), "2"),
    ((datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d"), "3"),
    ((datetime.datetime.now() + datetime.timedelta(days=4)).strftime("%Y-%m-%d"), "4"),
    ((datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y-%m-%d"), "5"),
    ((datetime.datetime.now() + datetime.timedelta(days=6)).strftime("%Y-%m-%d"), "6"),
    ((datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d"), "7"),
)


class Room(models.Model):
    type_room = models.CharField(max_length=100, choices=s)
    status = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)
    time_left = models.CharField(max_length=100, choices=times)
    order = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True)


class Order(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    comment = models.TextField()
    total_price = models.IntegerField()
