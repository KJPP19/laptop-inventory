from django.urls import path
from .views import RegisterApi, LogInApi



urlpatterns = [
    path('register/', RegisterApi.as_view()),
    path('login/', LogInApi.as_view())
]
