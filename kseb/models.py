from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 256)
    date = models.DateField(auto_now_add =True)
    compleated = models.BooleanField(default=False)

    def __str__(self):
        return self.title