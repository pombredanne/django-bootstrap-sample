from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=200)

class AnotherTest(models.Model):
    name = models.CharField(max_length=200)