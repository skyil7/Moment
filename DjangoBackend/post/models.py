from django.db import models

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    lat = models.IntegerField(null=False, default=0)
    lang = models.IntegerField(null=False, default=0)