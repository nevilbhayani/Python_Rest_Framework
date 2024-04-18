from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self) -> str:
        return self.title