from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=30)


class Account(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    release_date = models.DateField(verbose_name='Дата: YYYY-MM-dd')
    summa = models.IntegerField(verbose_name='Сумма')
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)
