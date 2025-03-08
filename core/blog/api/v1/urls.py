from django.urls import path,include
from blog.api.v1.views import *

app_name = 'api-v1'

urlpatterns = [
    path('post/',postlist,name='post-list'),
    path('post/<int:id>/',postDetail,name='post-detail')
]
