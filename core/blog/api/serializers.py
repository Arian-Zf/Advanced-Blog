from rest_framework import serializers
from blog.models import Post,Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class PostSerializer(serializers.ModelSerializer):

    # snippet = serializers.ReadOnlyField(source = 'get_snippet')
    # content = serializers.ReadOnlyField()
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category= serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(),many=False)
    # category = CategorySerializer(read_only=False)

    class Meta:
        model = Post
        fields = ['id','author','absolute_url','category','title','content','status','created_date','published_date','relative_url']
        # read_only_fields = ['content']

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep 
    
    

