from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]