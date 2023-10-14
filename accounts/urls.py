from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .forms import LoginForm
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
	path('register/', views.register, name='register'),
	path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
	path('dashboard/', views.dashboard, name='dashboard'),
]