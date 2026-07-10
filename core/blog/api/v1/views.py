from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404


# @api_view()
# def postlist(request):
#     posts = Post.objects.filter(status=True)
#     serializers = PostSerializer(posts,many=True)
#     return Response(serializers)

@api_view(["GET", "POST"])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data)



@api_view(["GET", "PUT", "DELETE"])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed"},status=status.HTTP_204_NO_CONTENT)




# @api_view()
# def postDetail(request,id):
#     post = get_object_or_404(Post,pk=id,status=True)
#     serializers = PostSerializer(post) # --> Dic
#     return Response(serializers.data) # --> json
    # except Post.DoesNotExist:
    #     return Response({"detail":"pose does not exist"},status=status.HTTP_404_NOT_FOUND)


    


    