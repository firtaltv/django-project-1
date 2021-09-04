from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('create', views.create, name='create'),
    path('profile', views.profile, name='profile'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.post_detail, name='detail')
]