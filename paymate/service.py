import datetime
from .models import Pay_nails


def pay_sum(name, values, term):
    """сумма за определенный отрезок времени"""
    pay_list = []
    t = datetime.datetime.now()
    for val in values:
        if term == 'month':
            if val.name == name and val.date.month == t.month:
                pay_list.append(val.pay_for_day)
            else:
                if val.name == name and val.date.year == t.year:
                    pay_list.append(val.pay_for_day)
    return sum(pay_list)


def counter(name, values):
    """колличество рабочих дней"""
    day = 0
    t = datetime.datetime.now()
    for val in values:
        if val.name == name and val.date.month == t.month:
            day += 1
    return day


def take_useful_value(request, bd):
    """Сбор нужных данных"""
    values = Pay_nails.objects.all()
    analytic_bd = bd()
    name = request.user
    date = datetime.datetime.now()
    return values, analytic_bd, name, date

