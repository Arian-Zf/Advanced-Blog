from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView 
from rest_framework import mixins


class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        """retrieveing a list of posts"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



# @api_view()
# def postlist(request):
#     posts = Post.objects.filter(status=True)
#     serializers = PostSerializer(posts,many=True)
#     return Response(serializers)

# @api_view(["GET", "POST"])
# def postList(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response (serializer.data)


# @api_view()
# def postDetail(request,id):
#     post = get_object_or_404(Post,pk=id,status=True)
#     serializers = PostSerializer(post) # --> Dic
#     return Response(serializers.data) # --> json
    # except Post.DoesNotExist:
    #     return Response({"detail":"pose does not exist"},status=status.HTTP_404_NOT_FOUND)



# @api_view(["GET", "PUT", "DELETE"])
# def postDetail(request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"item removed"},status=status.HTTP_204_NO_CONTENT)



# class PostList(APIView):

#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request):
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)




class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """ retrieving the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """ editing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """ deleting the post object """
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    


    


    