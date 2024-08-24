from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('lancar/', views.lancar, name='lancar'),
    path('alterar/', views.alterar, name='alterar'),
    path('visualizar/', views.visualizar, name='visualizar')

]

# EU QUE FIZ ESSE ARQUIVO #