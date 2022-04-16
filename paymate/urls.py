from django.urls import path
from . import views

app_name = 'paymate'

urlpatterns = [
    path('<int:pk>/update', views.PayUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.PayDeleteView.as_view(), name='pay_delete'),
    path('', views.pay_list, name='list'),
    path('<int:pk>', views.PayDetailView.as_view(), name='detail'),
    path('create/', views.createView, name='create'),
    path('statysticsM/', views.analyticMonth, name='staticM'),
    path('statysticsY/', views.analyticYear, name='staticY'),

]