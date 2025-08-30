from django.shortcuts import render, redirect
from .forms import TextoAnalizadoForm
from .models import TextoAnalizado, Palabra
from .preprocesamiento import clean_and_filter, frequencies
from django.core.files.base import ContentFile
from wordcloud import WordCloud
from io import BytesIO

def subir_texto(request):
    if request.method == 'POST':
        form = TextoAnalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # Procesar archivo subido
            try:
                file_path = instance.archivo.path
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    raw = f.read()
                tokens = clean_and_filter(raw)
                freq = frequencies(tokens)
                # Guardar tokens procesados en el propio texto
                try:
                    instance.tokens_json = list(tokens)
                    instance.save(update_fields=["tokens_json"])
                except Exception:
                    pass

                # Crear entradas Palabra asociadas al texto
                objs = [Palabra(texto=instance, contenido=tok, frecuencia=cnt) for tok, cnt in freq.items()]
                if objs:
                    Palabra.objects.bulk_create(objs)

                # Generar nube de palabras
                try:
                    wc = WordCloud(width=800, height=400, background_color="white", collocations=False)
                    wc.generate_from_frequencies(dict(freq))
                    buf = BytesIO()
                    wc.to_image().save(buf, format="PNG")
                    filename = f"wc_{instance.id}.png"
                    instance.nube_imagen.save(filename, ContentFile(buf.getvalue()), save=True)
                except Exception:
                    pass
            except Exception as e:
                # En un sistema real podríamos registrar el error con logging
                pass
            return redirect('lista_textos')
    else:
        form = TextoAnalizadoForm()
    return render(request, 'analisis/subir.html', {'form': form})

def lista_textos(request): 
    textos = TextoAnalizado.objects.all().order_by('-fecha_subida') 
    return render(request, 'analisis/lista.html', {'textos': textos})
