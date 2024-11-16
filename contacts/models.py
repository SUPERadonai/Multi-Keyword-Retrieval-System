from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Contact_new(models.Model):
    message = models.TextField(blank=True)
    house_id = models.IntegerField(blank=True)
    sub_id = models.IntegerField(blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.house_id


class Fav(models.Model):
    user_id = models.IntegerField(blank=True)
    sub_id = models.IntegerField(blank=True)
    type = models.IntegerField(blank=True)

    def __str__(self):
        return self.house_id
