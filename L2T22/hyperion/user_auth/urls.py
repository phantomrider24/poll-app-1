from django.urls import path, include, re_path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('login/', views.login, name='login'),
    path("create_user/", views.register_user, name="register_user"),
    path('polls/', include('polls.urls'))
]