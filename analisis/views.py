<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
=======
from django.shortcuts import render, redirect
>>>>>>> 76182a81822a6aa7a9c45c67f5f91222cbee9ddc
from .forms import TextoAnalizadoForm
from .models import TextoAnalizado, Palabra
from .preprocesamiento import clean_and_filter, frequencies
from django.core.files.base import ContentFile
<<<<<<< HEAD
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter
import nltk

def subir_texto(request):
    """
    Sube un archivo de texto, lo tokeniza, calcula frecuencias y genera
    un histograma de las palabras más frecuentes.
    """
    if request.method == 'POST':
        form = TextoAnalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.tipo_ngram = int(form.cleaned_data['tipo_ngram'])
            instance.calcular_probabilidades = form.cleaned_data['calcular_probabilidades']
            instance.save()
            
            try:
                # Leer archivo
                file_path = instance.archivo.path
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    raw = f.read()

                # Preprocesar
                tokens = clean_and_filter(raw)
                freq = frequencies(tokens)

                # Guardar tokens
                instance.tokens_json = list(tokens)
                instance.save(update_fields=["tokens_json"])

                # Guardar palabras en la base de datos
                objs = [
                    Palabra(texto=instance, contenido=tok, frecuencia=cnt)
                    for tok, cnt in freq.items()
                ]
                if objs:
                    Palabra.objects.bulk_create(objs)

                # Generar histograma de frecuencias
                top_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:20]
                if top_items:
                    palabras, counts = zip(*top_items)
                    plt.figure(figsize=(10, 5))
                    plt.bar(palabras, counts, color='skyblue')
                    plt.xticks(rotation=45, ha='right')
                    plt.xlabel("Palabras")
                    plt.ylabel("Frecuencia")
                    plt.title(f"Frecuencias de palabras - {instance.titulo}")
                    plt.tight_layout()

                    buf = BytesIO()
                    plt.savefig(buf, format="png")
                    plt.close()
                    filename = f"hist_{instance.id}.png"
                    instance.nube_imagen.save(filename, ContentFile(buf.getvalue()), save=True)

            except Exception as e:
                print(f"Error procesando archivo: {e}")

            # Redirigir según la opción seleccionada
            if instance.calcular_probabilidades:
                return redirect('ngram_mle', texto_id=instance.id)
            else:
                return redirect('lista_textos')
    else:
        form = TextoAnalizadoForm()

    return render(request, 'analisis/subir.html', {'form': form})

def lista_textos(request):
    """
    Muestra todos los textos procesados con sus histogramas y frecuencias.
    """
    textos = TextoAnalizado.objects.all().order_by('-fecha_subida')
    return render(request, 'analisis/lista.html', {'textos': textos})

def calcular_probabilidades_mle(tokens, n):
    """Calcula probabilidades MLE para n-gramas"""
    if n == 1:
        # Unigramas - probabilidades simples
        frecuencias = Counter(tokens)
        total = len(tokens)
        return {gram: (freq, freq/total) for gram, freq in frecuencias.items()}
    else:
        # N-gramas (n > 1) - probabilidades condicionales
        n_gramas = list(nltk.ngrams(tokens, n))
        n_minus_1_gramas = list(nltk.ngrams(tokens, n-1))
        
        freq_n_gramas = Counter(n_gramas)
        freq_n_minus_1_gramas = Counter(n_minus_1_gramas)
        
        probabilidades = {}
        for n_grama in freq_n_gramas:
            contexto = n_grama[:-1]  # Los n-1 tokens anteriores
            # Evitar división por cero
            count_contexto = freq_n_minus_1_gramas.get(contexto, 0)
            probabilidad = freq_n_gramas[n_grama] / count_contexto if count_contexto > 0 else 0
            probabilidades[n_grama] = (freq_n_gramas[n_grama], probabilidad)
        
        return probabilidades

def ngram_mle(request, texto_id):
    texto = get_object_or_404(TextoAnalizado, id=texto_id)
    n_valor = int(request.GET.get('n', texto.tipo_ngram))
    
    # Leer el contenido del archivo directamente
    try:
        with open(texto.archivo.path, 'r', encoding='utf-8', errors='ignore') as f:
            contenido = f.read()
    except Exception as e:
        return render(request, 'analisis/error.html', {
            'error': f'Error al leer el archivo: {e}'
        })
    
    # Tokenización básica (sin fronteras)
    tokens_sin = nltk.word_tokenize(contenido.lower())
    
    # Tokenización con fronteras de oración
    oraciones = nltk.sent_tokenize(contenido)
    tokens_con = []
    for s in oraciones:
        t = ['<s>'] + nltk.word_tokenize(s.lower()) + ['</s>']
        tokens_con.extend(t)
    
    # Calcular probabilidades
    mle_sin = calcular_probabilidades_mle(tokens_sin, n_valor)
    mle_con = calcular_probabilidades_mle(tokens_con, n_valor)
    
    # Preparar datos para el template
    resultados_sin = []
    for gram, (freq, prob) in mle_sin.items():
        resultados_sin.append({
            'gram': gram,
            'frecuencia': freq,
            'probabilidad': prob
        })
    
    resultados_con = []
    for gram, (freq, prob) in mle_con.items():
        resultados_con.append({
            'gram': gram,
            'frecuencia': freq,
            'probabilidad': prob
        })
    
    # Ordenar por frecuencia descendente
    resultados_sin.sort(key=lambda x: x['frecuencia'], reverse=True)
    resultados_con.sort(key=lambda x: x['frecuencia'], reverse=True)
    
    context = {
        "texto": texto,
        "n_valor": n_valor,
        "resultados_sin": resultados_sin,
        "resultados_con": resultados_con,
        "tokens_sin": tokens_sin[:50],  # Solo mostrar muestra
        "tokens_con": tokens_con[:50],  # Solo mostrar muestra
        "total_gramas_sin": len(resultados_sin),
        "total_gramas_con": len(resultados_con),
    }
    
    return render(request, "analisis/mle.html", context)
=======
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
>>>>>>> 76182a81822a6aa7a9c45c67f5f91222cbee9ddc
