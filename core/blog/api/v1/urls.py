from django.urls import path,include
from blog.api.v1.views import *

app_name = 'api-v1'

urlpatterns = [
    # path('post/',PostList.as_view(),name='post-list'),
    # path('post/<int:pk>/',PostDetail.as_view(),name='post-detail')
    path('post/',PostViewSet.as_view({"get":"list","post":"create"}),name='post-list'),
    path('post/<int:pk>/',PostViewSet.as_view({"get":"retrieve","put":"update","patch":"partial_update","delete":"destroy"}),name='post-detail'),
    
]
 