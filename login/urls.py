
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . forms import LoginForm

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('edit_user_profile/<str:user_id>/', views.edit_user_profile, name='edit_user_profile'),
  
    
    
]
