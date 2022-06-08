from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=50)
    option = models.TextField()

    def __str__(self):
        return f'[{self.pk}]{self.question}'
# Create your models here.
