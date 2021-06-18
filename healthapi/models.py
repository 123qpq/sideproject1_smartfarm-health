from django.db import models

# Create your models here.
class healthdata(models.Model):
    user =  models.CharField(max_length=20)
    temperature = models.DecimalField(max_digits=5, decimal_places=2) #최대 5자리, 소숫점은 2자리까지
    heartrate = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add = True, blank=True, null=True)#생성 시 현재 시간 자동 저장
