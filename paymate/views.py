from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from .models import Pay_nails, AnalyticMonth, AnalyticYear
from .forms import Pay_nailsForm


@login_required
def pay_list(request):
    nails_values = Pay_nails.objects.all()
    return render(request, 'paymate/list.html', {'nails_values': nails_values})


@login_required
def createView(request):
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


class PayDetailView(LoginRequiredMixin, DetailView):
    model = Pay_nails
    template_name = 'paymate/details.html'
    context_object_name = 'from_name'
    raise_exception = True


class PayUpdateView(LoginRequiredMixin, UpdateView):
    model = Pay_nails
    template_name = 'paymate/update.html'
    fields = ['nails_for_day', 'pay_for_day']
    raise_exception = True


class PayDeleteView(LoginRequiredMixin, DeleteView):
    model = Pay_nails
    success_url = '/'
    template_name = 'paymate/delete.html'
    raise_exception = True


@login_required
def analyticMonth(request):
    values = Pay_nails.objects.all()
    analM = AnalyticMonth()
    name = request.user
    mon = datetime.datetime.now()
    analM.pay_for_month = month(name, values)
    analM.medium_pay = month(name, values)/counter(name, values)
    analM.name = request.user
    analM.month = mon.month
    analM.save()
    return render(request, 'paymate/statystics.html', {'analM': analM})


def month(name, values):
    monthPay = []
    t = datetime.datetime.now()
    for val in values:
        if val.name == name and val.date.month == t.month:
            monthPay.append(val.pay_for_day)
    return sum(monthPay)


@login_required
def analyticYear(request):
    values = Pay_nails.objects.all()
    analY = AnalyticYear()
    name = request.user
    mon = datetime.datetime.now()
    analY.pay_for_year = year(name, values)
    analY.medium_pay = year(name, values)/12
    analY.name = request.user
    analY.year = mon.year
    analY.save()
    return render(request, 'paymate/year.html', {'analY': analY})


def year(name, values):
    yearPay = []
    t = datetime.datetime.now()
    for val in values:
        if val.name == name and val.date.year == t.year:
            yearPay.append(val.pay_for_day)
    return sum(yearPay)


def counter(name, values):
    day = 0
    t = datetime.datetime.now()
    for val in values:
        if val.name == name and val.date.month == t.month:
            day += 1
    return day
