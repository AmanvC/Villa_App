from django.db import models
from django.urls import reverse

class Villa(models.Model):
    number = models.PositiveIntegerField()
    block = models.PositiveIntegerField()

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('basic_app:list')

class Owner(models.Model):
    name = models.CharField(max_length=264)
    age = models.PositiveIntegerField()
    mobile = models.PositiveIntegerField()
    villa = models.ForeignKey(Villa, related_name='owners', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:list')
