from django.urls import path
from . import views
from django.views.generic import TemplateView, RedirectView



urlpatterns = [
    # path('num1',views.indexView,name='indexView'),
    # path('num2', TemplateView.as_view(template_name="index.html", extra_context={"name": "ali"})),
    # path('cbv-index', views.IndexView.as_view(),name='cbv-index'),
    # path('go-to-maktabkhooneh/<int:pk>/', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),


    path('post_list', views.PostList.as_view(),name='post_list'),
    path('post/<int:pk>/', views.PostListDetail.as_view(),name='post_list_detail'),


]