from django.urls import path,include
from . import views




urlpatterns = [

    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    # path('postDetail/<int:id>/', views.postDetail,name='post_detail'),
    # path('post/', views.postList,name='post_detail')

    path('post/', views.PostList.as_view(),name='post_detail'),
    path('postDetail/<int:id>/', views.PostDetail.as_view(),name='post_detail'),

]