from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=80, default='Default Title')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    lat = models.IntegerField(null=False, default=0)
    lng = models.IntegerField(null=False, default=0)
    img = models.TextField(null=True)