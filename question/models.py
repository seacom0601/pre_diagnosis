from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=50)

    option1 = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.pk}]  {self.question}'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField(max_length=20)

    def __str__(self):
        return self.option


class AnsUser(models.Model):
    phone_num = models.CharField(max_length=13, default="000-0000-0000")
    answer = models.CharField(default="", max_length=20, null=True, blank=True)

    def __str__(self):
        return self.phone_num
