from django.db import models

#Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=180)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def _str_(self):
        return self.title
