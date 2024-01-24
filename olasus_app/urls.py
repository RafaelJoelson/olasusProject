from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # outras configurações de URL, se houver
]