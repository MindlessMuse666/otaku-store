from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(next_page='core:home'), name='account_logout'),
] 