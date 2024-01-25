from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.modulo_acs, name='modulo_acs'),
    # outras configurações de URL, se houver
]