from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'duolinguas'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastroUsuario'),
    path('usuarios/', views.usuarios, name='list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


