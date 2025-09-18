from django.db import models

class TextoAnalizado(models.Model):
    tokens_json = models.JSONField(default=list, blank=True)
    nube_imagen = models.ImageField(upload_to='wordclouds/', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='textos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    tipo_ngram = models.IntegerField(default=2)  # Nuevo campo
    calcular_probabilidades = models.BooleanField(default=False)  # Nuevo campo

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Leer el contenido del archivo al guardar
        if self.archivo:
            self.archivo.seek(0)  # Asegurarse de estar al inicio
            self.contenido = self.archivo.read().decode('utf-8', errors='ignore')
        super().save(*args, **kwargs)

class Palabra(models.Model):
    texto = models.ForeignKey(TextoAnalizado, on_delete=models.CASCADE, related_name='palabras')
    contenido = models.CharField(max_length=100)
    frecuencia = models.IntegerField()

    def __str__(self):
        return f"{self.contenido}: {self.frecuencia}"