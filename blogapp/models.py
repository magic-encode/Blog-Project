from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    title_1 = models.CharField(max_length=200)
    description_1 = models.TextField(null=True, blank=True)
    title_2 = models.CharField(max_length=200)
    description_2 = models.TextField(null=True, blank=True)
    title_3 = models.CharField(max_length=200)
    description_3 = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
class Catagory(models.Model):
    catagory = models.CharField(max_length=250)
    

class Comments(models.Model):
    item = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="comment", null=True, blank=True)
    person = models.ForeignKey(
        User, related_name="user", on_delete=models.DO_NOTHING, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
