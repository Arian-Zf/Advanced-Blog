from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('num1',views.indexView,name='indexView'),
    # path('num2', TemplateView.as_view(template_name="index.html", extra_context={"name": "ali"})),
    path('cbv-index', views.IndexView.as_view(),name='cbv-index'),
]