
from django.urls import path
from beneficiario import views

app_name = 'beneficiario'

urlpatterns = [
    path('', views.index, name='index'),
]
