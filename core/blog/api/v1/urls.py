from django.urls import path,include
from . import views




urlpatterns = [

    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    
]