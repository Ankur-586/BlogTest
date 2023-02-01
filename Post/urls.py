from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='BlogHome'),
    path('<int:pk>/', views.blogview, name='BLOGVIEW'),
    path('post/', views.add_posts, name="POSTS"),
    path('update/<int:id>/',views.update_rec, name="Update"),
    path('delete/<int:id>/',views.delete_rec,name='Delete'),
    path('about/',views.About_us,name='About'),
    path('userdashboard/',views.userdashboard,name='UserDashboard'),
]