from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import PostSerializer
from blog.models import Post
from rest_framework import status


@api_view()
def postlist(request):
    return Response("ok")



@api_view()
def post_detail(request,id):
    try:
        post = Post.objects.get(id=id)
        serializers = PostSerializer(post) # --> Dic
        return Response(serializers.data) # --> json
    except Post.DoesNotExist:
        return Response({"detail":"pose does not exist"},status=status.HTTP_404_NOT_FOUND)


    


    