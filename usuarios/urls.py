from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
]

# EU QUE FIZ ESSE ARQUIVO #