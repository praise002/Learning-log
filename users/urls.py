from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # Include the default auth urls
    path('', include('django.contrib.auth.urls')),
    
    #Registration page
    path('register/', views.register, name='register'),

    # path('logout/', views.logout, name='logout'),
]
