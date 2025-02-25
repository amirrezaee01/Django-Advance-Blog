from django.urls import path,include
from blog.views import *
from django.views.generic.base import RedirectView,TemplateView

app_name = 'blog'
 
urlpatterns = [
    # path('cbv-index', Indexview.as_view(), name= 'cbv-index'),
    # path('go-to-maktabkhooneh',RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh')
    path('post/', PostListView.as_view(), name= 'post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post-detail'),
    path('post/create/', PostCreateView.as_view(), name= 'post-create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name= 'post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name= 'post-delete'),
    path('api/v1/',include('blog.api.v1.urls'))
]
