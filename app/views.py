from rest_framework import generics, viewsets, views, parsers, response
from app import models, serializers


class PostListAPIView(generics.ListAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostSerializer


class PostAddAPIView(generics.CreateAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostSerializer


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostSerializer


class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostSerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CustomFormAPIView(views.APIView):
    parser_classes = (parsers.MultiPartParser, parsers.FileUploadParser)
    http_method_names = ['post', 'get',]

    def get(self, request, format=None):
        return response.Response({'status': True})

    def post(self, request, fromat=None):
        serializer_data = serializers.FormSerializers(data=self.request.data)
        serializer_data.is_valid(raise_exception=True)
        return response.Response(serializer_data.data)

    def delete(self):
        return response.Response({'status': 'deleted'})
    
