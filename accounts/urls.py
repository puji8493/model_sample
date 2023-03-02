from django.urls import path
from . import views

app_name = 'accounts'

# http://127.0.0.1:8000/accounts/signup/

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
