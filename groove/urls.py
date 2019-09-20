from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
  ##AUTH
  path('signup', views.SignUp.as_view(), name="signup"),
  path('login', auth_views.LoginView.as_view(), name='login'),
  path('logout', auth_views.LogoutView.as_view(), name="logout"),
  ##DASHBOARD
  path('dashboard', views.dashboard, name='dashboard'),
  ##GROOVES
  path('create_groove', views.CreateGroove.as_view(), name="create_groove"),
  path('groove/<int:pk>', views.DetailGroove.as_view(), name='detail_groove'),
  path('groove/<int:pk>/update', views.UpdateGroove.as_view(), name='update_groove'),
  path('groove/<int:pk>/delete', views.DeleteGroove.as_view(), name='delete_groove'),
  path('grooves', views.all_grooves, name="grooves")
]