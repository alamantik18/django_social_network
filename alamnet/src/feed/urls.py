from django.urls import path
from .views import FeedView

urlpatterns = [
    path('<int:pk>', FeedView.as_view({'get': 'retreview'})),
    path('', FeedView.as_view({'get': 'list'})),
]