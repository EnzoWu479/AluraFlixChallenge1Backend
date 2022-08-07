from django.apps import AppConfig


class VideosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videos'
    def ready(self):
        from .models import Categoria
        if not Categoria.objects.exists():
            categoria = Categoria.objects.create(
                titulo = "Livre",
                cor="#000"
            )
            categoria.save()
