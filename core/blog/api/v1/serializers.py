from rest_framework import serializers
from ...models import Post


#simple serializer like form that you have to full fill it by yourself
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     author = serializers.EmailField()
 
class PostSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Post  
        fields = ['id', 'author','title', 'content', 'status', 'createed_date', 'published_date']