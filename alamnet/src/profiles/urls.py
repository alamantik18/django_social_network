from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.GetUserView.as_view()),
]