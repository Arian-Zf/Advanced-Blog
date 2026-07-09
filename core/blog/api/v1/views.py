from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import PostSerializer
from blog.models import Post


@api_view()
def postlist(request):
    return Response("ok")



@api_view()
def post_detail(request,id):
    post = Post.objects.get(id=id)
    serializers = PostSerializer(post) # --> Dic
    return Response(serializers.data) # --> json


    