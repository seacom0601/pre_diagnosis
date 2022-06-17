from django.db import models

# Create your models here.


# 환자 정보 테이블
class Patient(models.Model):
    patient_code = models.CharField(default="000000", max_length=6, blank=False, primary_key=True)
    name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f'[{self.patient_code}] {self.name}'

# 사용자 테이블
class User(models.Model):
    patient_code = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sick_parts = models.CharField(default="", max_length=100, null=True, blank=False)
    answer = models.TextField(default="", max_length=1000, blank=False)

    def __str__(self):
        return f'[{self.pk}] {self.patient_code}'
