from django.urls import path
from .views import SignUpView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]
