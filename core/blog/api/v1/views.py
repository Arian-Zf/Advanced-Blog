from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view()
def postlist(request):
    posts = Post.objects.filter(status=True)
    serializers = PostSerializer(posts,many=True)
    return Response(serializers)



@api_view()
def post_detail(request,id):
    post = get_object_or_404(Post,pk=id,status=True)
    serializers = PostSerializer(post) # --> Dic
    return Response(serializers.data) # --> json
    # except Post.DoesNotExist:
    #     return Response({"detail":"pose does not exist"},status=status.HTTP_404_NOT_FOUND)


    


    