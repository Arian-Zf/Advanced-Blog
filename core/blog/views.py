from django.shortcuts import render
from .models import *
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import PostForm



'''def indexView
def indexView(request):
    return render(request,'index.html')
'''


'''TemplateView
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context'''

    

''' RedirectView

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
'''



class PostList(ListView):
    # queryset = Post.objects.all()
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

class PostListDetail(DetailView):
    model = Post

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/thanks/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class PostCreateView(CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

