from django.urls import path, include
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login_user', views.login_user, name="login_user")
]
