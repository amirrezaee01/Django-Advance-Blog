from django.db import models
from django.contrib.auth import get_user_model

#getting user model
#User = get_user_model()


class Post(models.Model):
    '''
    This class defines the structure for blog posts in the blog app.
    '''
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    createed_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title


class Category(models.Model):
    """
    This class defines the structure for categories used to group blog posts.
    """
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
