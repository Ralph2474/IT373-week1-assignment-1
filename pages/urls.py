from django.urls import path
from pages import views
urlpatterns = [
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
]
