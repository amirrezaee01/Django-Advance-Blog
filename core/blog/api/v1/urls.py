from django.urls import path,include
from blog.api.v1.views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'


router = DefaultRouter()
router.register('post',PostModelViewSet, basename='post')
router.register('category',CategoryModelViewSet, basename='category')
urlpatterns = router.urls


