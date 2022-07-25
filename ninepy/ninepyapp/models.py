from django.db import models

from taggit.managers import TaggableManager
# Create your models here.



class Questions(models.Model):
    question = models.TextField()
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()
    e = models.TextField(default=None)
    answer = models.TextField()
    explanation = models.TextField(max_length=1024, default=None)
    tags = TaggableManager()

    class Meta:
        db_table = 'Questions'

