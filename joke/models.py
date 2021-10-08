from django.db import models

# Create your models here.
class Joke(models.Model):
    joke=models.TextField()