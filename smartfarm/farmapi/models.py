from django.db import models

# Create your models here.

class farminfo(models.Model):
    farmid = models.CharField(max_length=20, primary_key=True)
    toggle = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.farmid}'

class farmdata(models.Model):
    farmid = models.ForeignKey("farminfo", on_delete=models.CASCADE)
    moisture = models.DecimalField(max_digits=5, decimal_places=2) #최대 5자리, 소숫점은 2자리까지
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    barometric = models.DecimalField(max_digits=5, decimal_places=2)
    altitude = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add = True)#생성 시 현재 시간 자동 저장
    def __str__(self):
        return f'{self.datetime}'

