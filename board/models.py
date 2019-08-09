from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import re

class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)#User 를 Foreign Key로
    date = timezone.localtime()
    content = models.TextField()
    location = models.TextField()
    tag_set = models.ManyToManyField('Tag', related_name='tag', blank=True)
    #category = models.ForignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def createdDate(self):
        return self.date.date()

    def __str__(self):
        return self.title

    def tag_save(self):
        self.tag_set.clear()
        tags = re.findall(r'#(\w+)\b', self.content)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # ManyToManyField 에 인스턴스 추가

class Tag(models.Model):
    name=models.CharField(max_length=80, unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name