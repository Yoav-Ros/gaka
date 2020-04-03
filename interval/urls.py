from django.urls import path
from . import views



urlpatterns = [
   path('learn/', views.learn, name='learn'),
   path('score/', views.score, name='score'),
   path('practice/', views.choose_practice, name='choose_practice'),
   path('practice/<str:question>', views.practice, name='practice'),
]
