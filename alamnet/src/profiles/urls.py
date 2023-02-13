from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>', views.UserPublicView.as_view({'get': 'retrieve'})),
]