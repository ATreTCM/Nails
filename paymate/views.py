from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Analytic_month, Analytic_year
from .forms import Pay_nailsForm
from .service import *


@login_required
def works_day_list(request):
    """Список отработанных дней с результатами"""
    nails_values = Pay_nails.objects.all()
    return render(request, 'paymate/list.html', {'nails_values': nails_values})


@login_required
def create_works_day_list(request):
    """Запись результата трудового дня"""
    if request.method == 'POST':
        value_form = Pay_nailsForm(request.POST)
        if value_form.is_valid():
            new = value_form.save(commit=False)
            new.name = request.user
            new.pay_for_day = int(new.nails_for_day) * 0.07
            new.save()
            return redirect('paymate:list')
    else:
        value_form = Pay_nailsForm()
    return render(request, 'paymate/create.html', {'value_form': value_form})


class Works_day_detail(LoginRequiredMixin, DetailView):
    """Результат определенного трудового дня"""
    model = Pay_nails
    template_name = 'paymate/details.html'
    context_object_name = 'from_name'
    raise_exception = True


class Update_works_day(LoginRequiredMixin, UpdateView):
    """Редактирование результата трудового дня"""
    model = Pay_nails
    template_name = 'paymate/update.html'
    fields = ['nails_for_day', 'pay_for_day']
    raise_exception = True


class Delete_works_day(LoginRequiredMixin, DeleteView):
    """Удаление результатов трудового дня"""
    model = Pay_nails
    success_url = '/'
    template_name = 'paymate/delete.html'
    raise_exception = True


@login_required
def analytic_month(request):
    """Сохранение данных за месяц"""
    values, analytic_bd, name, date = take_useful_value(request, Analytic_month)
    analytic_bd.pay_for_month = pay_sum(name, values, 'month')
    if counter(name, values) == 0:
        analytic_bd.medium_pay = pay_sum(name, values, 'month')
    else:
        analytic_bd.medium_pay = pay_sum(name, values, 'month')/counter(name, values)
    analytic_bd.name = name
    analytic_bd.month = date.month
    analytic_bd.save()
    return render(request, 'paymate/statystics.html', {'analytic_bd': analytic_bd})


@login_required
def analytic_year(request):
    """Сохранение данных за год"""
    values, analytic_bd_y, name, date = take_useful_value(request, Analytic_year)
    analytic_bd_y.pay_for_year = pay_sum(name, values, 'year')
    analytic_bd_y.medium_pay = pay_sum(name, values, 'year')
    analytic_bd_y.name = name
    analytic_bd_y.year = date.year
    analytic_bd_y.save()
    return render(request, 'paymate/year.html', {'analytic_bd_y': analytic_bd_y})


