from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from .views import home

urlpatterns = [
    path('', include('leads.urls')),
    path('', include('frontend.urls')),
    path('admin', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),  # <- Here
    path(r'home', home, name='home'),

]