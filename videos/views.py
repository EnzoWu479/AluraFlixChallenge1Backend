from rest_framework import viewsets, generics, filters
from .models import Video, Categoria
from .serializer import VideoSerializer, CategoriaSerializer, VideosInCategoriasSerializer, FreeVideosSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from users.jwt import JWTAuth

class VideoViewSet(viewsets.ModelViewSet):
    '''Todos os videos'''
    queryset = Video.objects.all()
    authentication_classes = (JWTAuth,)
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo']
    search_fields = ['titulo', 'descricao']

class CategoriaViewSet(viewsets.ModelViewSet):
    '''Todas as categorias'''
    authentication_classes = (JWTAuth,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class VideosInCategorias(generics.ListAPIView):
    """Listando is videos de uma categoria"""
    authentication_classes = (JWTAuth,)
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = VideosInCategoriasSerializer

class freeVideos(generics.ListAPIView):
    '''Listando videos grátis'''
    def get_queryset(self):
        queryset = Video.objects.filter(premium=False)
        return queryset
    serializer_class = FreeVideosSerializer
    
    