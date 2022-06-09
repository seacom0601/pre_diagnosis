from django.db import models

# Create your models here.


# 부위 테이블
class Sickpart(models.Model):
    name = models.CharField(max_length=20, blank=False, primary_key=True)

    def __str__(self):
        return self.name


# 선지 테이블
class Option(models.Model):
    option = models.CharField(max_length=50, blank=False, primary_key=True)

    def __str__(self):
        return self.option


# 질문 테이블
class Question(models.Model):
    question = models.CharField(max_length=200, blank=False, unique=True)
    video = models.CharField(max_length=200, null=True)
    option = models.ForeignKey(Option, on_delete=models.RESTRICT)
    sick_part = models.ForeignKey(Sickpart, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.sick_part}] {self.question}'
