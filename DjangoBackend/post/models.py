from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=80, default='Default Title')
    category = models.CharField(max_length=80, default='Default Category')
    date = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    lat = models.IntegerField(null=True)
    lng = models.IntegerField(null=True)
    img = models.ImageField(null=True)
    

class Image(models.Model):
    img = models.ImageField(blank=True)