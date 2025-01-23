from django.shortcuts import render 
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView
from blog.models import Post
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
