from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import PostSerializer,CategorySerializer
from blog.models import Post,Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly




class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    @action(methods=["get"], detail=False)
    def get_ok(self, request):
        return Response({'detail': 'ok'})

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

#     def list(self, request):
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def partial_update(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def destroy(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         post_object.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class PostList(ListCreateAPIView):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)



# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)



# class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     """getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

#     def get(self, request, *args, **kwargs):
#         """retrieveing a list of posts"""
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



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




# class PostDetail(APIView):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         """ retrieving the post data """
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)

#     def put(self, request, id):
#         """ editing the post data """
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = PostSerializer(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def delete(self, request, id):
#         """ deleting the post object """
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"detail": "item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    


    


    