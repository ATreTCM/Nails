from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Pay_nails(models.Model):
    """Таблица работы за день"""
    name = models.ForeignKey(User, on_delete=models.CASCADE, unique_for_date='publish')
    pay_for_day = models.DecimalField(max_digits=100, decimal_places=2, default=0, verbose_name='оплата за день')
    nails_for_day = models.DecimalField(max_digits=100, decimal_places=2, default=0, verbose_name='кол-во гвоздей')
    date = models.DateField(auto_now_add=True, unique_for_date=True)
    objects = models.Manager()


    def get_absolute_url(self):
        return reverse('paymate:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['date']


class Analytic_month(models.Model):
    """Таблица работы за месяц"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    pay_for_month = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    medium_pay = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    month = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    objects = models.Manager()


class Analytic_year(models.Model):
    """Таблица работы за год"""
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    medium_pay = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    pay_for_year = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    year = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    objects = models.Manager()