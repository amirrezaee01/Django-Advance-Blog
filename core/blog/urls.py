from django.urls import path
from blog.views import *
from django.views.generic.base import RedirectView,TemplateView

app_name = 'blog'

urlpatterns = [
    path('cbv-index', Indexview.as_view(), name= 'cbv-index'),
    path('go-to-maktabkhooneh',RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh')
]
