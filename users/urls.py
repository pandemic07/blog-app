# users/urls.py
from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterView,LoginView,LogoutView, UserView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register-user'),
    path('login', LoginView.as_view(), name='user-login'),  # Use the built-in view for login
    path('logout', LogoutView.as_view(), name='user-logout'),
    path('user', UserView.as_view(), name='user-logout'),
]
