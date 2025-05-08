from django.contrib import admin
from django.urls import path
from newsletter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_newsletter, name='create'),
]
