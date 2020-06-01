from django.contrib import admin
from django.urls import path, include
from bugtrack import views
from register import views as reg_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register/', reg_view.register, name='register'),
    path('', include('django.contrib.auth.urls')),
]
