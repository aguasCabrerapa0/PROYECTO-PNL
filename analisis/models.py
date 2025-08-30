from django.db import models

# Create your models here.
class TextoAnalizado(models.Model):
    tokens_json = models.JSONField(default=list, blank=True)
    nube_imagen = models.ImageField(upload_to='wordclouds/', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='textos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo



class Palabra(models.Model):
    texto = models.ForeignKey(TextoAnalizado, on_delete=models.CASCADE, related_name='palabras')
    contenido = models.CharField(max_length=100)
    frecuencia = models.IntegerField()

    def __str__(self):
        return f"{self.contenido}: {self.frecuencia}"