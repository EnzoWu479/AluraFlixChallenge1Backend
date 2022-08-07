from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from videos.views import VideoViewSet, CategoriaViewSet, VideosInCategorias, freeVideos

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename="Videos")
router.register('categorias', CategoriaViewSet, basename="Categorias")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categorias/<int:pk>/videos/', VideosInCategorias.as_view()),
    path('videos/free', freeVideos.as_view()),
    path('users/', include('users.urls'))
]
