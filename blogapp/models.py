from django.db import models
from django.contrib.auth.models import User


class Catagory(models.Model):
    catagory = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.catagory


class Blog(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.DO_NOTHING, related_name='Catagorys')
    image_1 = models.ImageField()
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    title_1 = models.CharField(max_length=200)
    description_1 = models.TextField()
    title_2 = models.CharField(max_length=200, null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    title_3 = models.CharField(max_length=200, null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_1


class Comments(models.Model):
    person = models.ForeignKey(
        User, related_name="user", on_delete=models.DO_NOTHING, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.person.username
    