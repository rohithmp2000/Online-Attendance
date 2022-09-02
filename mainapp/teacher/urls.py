from django.urls import path, include
from . import views

urlpatterns = [
    path('teacher1/', views.hello),
]