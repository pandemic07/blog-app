from django.urls import path
from .views import RegisterView,LoginView,LogoutView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user'),
    path('login/', LoginView.as_view(), name='user-login'), 
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('user/', UserView.as_view(), name='user-logout'),
]
