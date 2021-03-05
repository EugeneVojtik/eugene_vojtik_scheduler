from django.urls import path

from authentication_app.views import RegisterAPI, CreateToken, LoginUser

urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register_user'),
    path('create_token', CreateToken.as_view(), name='create_token'),
    path('login', LoginUser.as_view(), name='login_user'),
]
