from django.urls import path
from . import views

urlpatterns = [
    path('booth/', views.booth, name='booth'),
    path('foodtruck/', views.foodtruck, name='foodtruck'),
    path('lineup/', views.lineup, name='lineup'),
    path('bus/', views.bus, name='bus'),
    path('booth/individual/', views.individual, name="individual"),
    path('booth/organization/', views.organization, name="organization"),
]