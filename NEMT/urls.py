from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),        # base.html
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('accounts/login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
