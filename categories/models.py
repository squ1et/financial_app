from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=30)
    body = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={"pk": self.pk})


        
