from django.db import models

# Create your models here.
class Hashtag(models.Model):
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title
class Products(models.Model):
    title = models.TextField(max_length=255)
    opis = models.TextField(max_length=255)
    price = models.IntegerField(null=True)
    creat_date = models.DateField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag)

