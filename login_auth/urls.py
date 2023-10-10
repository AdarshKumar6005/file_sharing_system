from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='login'),
    path('login/', views.login, name='login'),
]