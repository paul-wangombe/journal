from django.db import models

# Create your models here.


class Journal(models.Model):
    date = models.DateTimeField()
    title = models.CharField(blank=True, max_length=140)
    body = models.TextField()

    def __str__(self):
        return self.title
