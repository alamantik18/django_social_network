from django.urls import path
from .views import *

urlpatterns = [
    path('comment', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('post', PostView.as_view({'post': 'create'})),
    path('post/<int:pk>', PostView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>', PostListView.as_view())
]