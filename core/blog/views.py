from django.shortcuts import render 
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView,DeleteView,FormView,CreateView,UpdateView
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import get_object_or_404


#function base view to show a template
""""
def index_view(request):
    name = 'ali'
    context = {'name':name}
    return render(request,'index.html',context)
"""
class Indexview(TemplateView):
    template_name = 'index.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context
""""
FBV for redirect
from django.shortcuts import redirect 
def RedirectTOMaktab(request):
    return redirect ("https://maktabkhoneh.com")
"""

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'
    
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)

        return super().get_redirect_url(*args, **kwargs)

class PostListView(LoginRequiredMixin,ListView):
    
    model = Post
    context_object_name = 'posts'
    # paginate_by = 2
    ordering = 'id'
    #permission_required = "blog.add_post"
    # queryset = Post.objects.all()
    # def get_queryset():
    # posts = Post.object.filter(status=true)
    # return posts
    
    
class PostDetailView(DeleteView):
    model = Post
 
""""   
#create post by FormView
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
"""
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'
    

    