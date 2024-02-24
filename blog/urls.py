from django.urls import path
from .views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/update/', post_update, name='post_update'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]
