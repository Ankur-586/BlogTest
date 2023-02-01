from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.register,name='Register'),
    path('login/',views.user_login,name='Login'),
    path('logout/',views.user_logout,name='Logout'),
]