from django.urls import path
from . import views

app_name = 'paymate'

urlpatterns = [
    path('<int:pk>/update', views.Update_works_day.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete_works_day.as_view(), name='pay_delete'),
    path('', views.works_day_list, name='list'),
    path('<int:pk>', views.Works_day_detail.as_view(), name='detail'),
    path('create/', views.create_works_day_list, name='create'),
    path('statysticsM/', views.analytic_month, name='staticM'),
    path('statysticsY/', views.analytic_year, name='staticY'),

]