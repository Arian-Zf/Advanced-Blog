from django.shortcuts import render
from .models import *
from django.views.generic.base import TemplateView




def indexView(request):
    return render(request,'index.html')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context