from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from django.shortcuts import render
from api.serializers import PostSerializer, TranslationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from api.models import Post, Translation

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = (AllowAny,)

    def list(self, request):
        """
        Given a username parameter, returns only the translations that the
        post specified
        """
        pdb.set_trace()
        queryset = Post.objects.all()
        post = request.query_params.get('post', None)
        if post is not None:   
            queryset = Link.objects.filter(post__id=post)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)