# Import required modules
from django.urls import path

from register import views
from register.views import login_view, register

# Set app name
app_name = 'register'

# Define URL patterns for the register app
urlpatterns=[
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout_user', views.logout_view, name='1234'),
]
