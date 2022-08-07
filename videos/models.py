from django.db import models
class Categoria(models.Model):
    titulo = models.CharField(max_length=255, default="")
    cor = models.CharField(max_length=9, default='#000')
    def __str__(self):
        return self.titulo
    def save(self, *args, **kwargs):
        super(Categoria, self).save(*args, **kwargs)


class Video(models.Model):
    def default():
        return Categoria.objects.get(titulo="Livre")
    
    titulo = models.CharField(max_length=255, default="")
    descricao = models.TextField(max_length=1000, default="", blank=True)
    url = models.CharField(max_length=1000, default="")
    premium = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=default)
    def __str__(self):
        return self.titulo



