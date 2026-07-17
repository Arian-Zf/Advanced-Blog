from rest_framework import serializers
from blog.models import Post,Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):

    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    content = serializers.ReadOnlyField()
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id','author','get_abs_url','title','content','snippet','status','created_date','published_date','relative_url']
        # read_only_fields = ['content']

    def absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

