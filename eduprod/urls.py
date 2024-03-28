from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flashcard/', views.index, name='flashcard')  # Corrected URL path
]
