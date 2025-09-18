<<<<<<< HEAD
Procesamiento de Lenguaje Natural - Sistema de Análisis de Texto
Este proyecto es una aplicación web Django para el análisis de textos utilizando técnicas de Procesamiento de Lenguaje Natural (NLP). Incluye tokenización, cálculo de frecuencias, n-gramas y probabilidades condicionales usando el enfoque de Máxima Verosimilitud (MLE).

🚀 Características
✅ Subida y procesamiento de archivos de texto

✅ Tokenización y limpieza de texto

✅ Cálculo de frecuencias de palabras

✅ Generación de histogramas de frecuencias

✅ Análisis de n-gramas (unigramas, bigramas, trigramas, etc.)

✅ Cálculo de probabilidades condicionales (MLE)

✅ Comparación con y sin fronteras de oración

✅ Interfaz web amigable

📋 Requisitos Previos
Python 3.8+

pipenv (entorno virtual)

Git

🛠️ Instalación
1. Clonar el repositorio
bash
git clone https://github.com/aguasCabrerapa0/PROYECTO-PNL.git
cd "Procesamiento de lenguaje natural"
2. Configurar entorno virtual con pipenv
bash
# Instalar pipenv si no lo tienes
pip install pipenv

# Crear entorno virtual e instalar dependencias
pipenv install
3. Instalar datos de NLTK
bash
# Activar el entorno virtual
pipenv shell

# Descargar los datos necesarios de NLTK
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"
4. Configurar la base de datos
bash
# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate
5. Crear superusuario (opcional)
bash
python manage.py createsuperuser
🚀 Ejecución
bash
# Activar el entorno virtual (si no está activo)
pipenv shell

# Ejecutar el servidor de desarrollo
python manage.py runserver
Abrir en el navegador: http://127.0.0.1:8000/

📖 Uso del Sistema
1. Subir un texto
Haz clic en "Subir nuevo texto"

Completa el título

Selecciona el archivo de texto

Elige el tipo de n-grama (1-5)

Marca la opción "Calcular probabilidades MLE" si deseas análisis avanzado

Haz clic en "Subir y Analizar"

2. Ver resultados
Lista de textos: Muestra todos los textos procesados con sus frecuencias

Probabilidades MLE: Muestra análisis detallado con y sin fronteras de oración

3. Análisis MLE
El sistema calcula:

Probabilidades condicionales usando Máxima Verosimilitud

Comparación con fronteras de oración (<s> y </s>)

Tablas de frecuencias y probabilidades

Estadísticas comparativas
=======
# Cómo ejecutar el proyecto (PLN avance 2)

## Requisitos
- Python 3.10+
- (Opcional) pipenv

## Pasos
```bash
cd "/mnt/data/PLN_avance2_extracted/Procesamiento de lenguaje natural"
# Entorno
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # instala Django

# Migraciones y arranque
python manage.py migrate
python manage.py runserver
```

Luego abre http://127.0.0.1:8000/

## Limpieza integrada (minúsculas, sin puntuación, sin stopwords)
El flujo de carga ahora procesa el archivo de texto y:
- Convierte a minúsculas.
- Elimina signos de puntuación (se extraen solo tokens alfabéticos).
- Elimina stopwords en español (lista incorporada).
- Calcula frecuencias y llena el modelo `Palabra`.

### Dónde está la lógica
- `analisis/preprocesamiento.py`: STOPWORDS + funciones `clean_and_filter` y `frequencies`.
- `analisis/views.py`: en `subir_texto`, después de `form.save()` se lee el archivo, se limpia, se tokeniza y se guardan frecuencias.

## Verificación
1) Sube un `.txt` en `/subir/`.
2) Vuelve a la página principal y confirma que aparecen tokens y frecuencias bajo el título.
3) De ser necesario, borra `db.sqlite3` para reiniciar datos y repite pruebas.

## Commit sugerido
Si tu proyecto está versionado con Git, ejecuta desde la raíz del proyecto:
```bash
git add analisis/preprocesamiento.py analisis/views.py README_CORRER_PROYECTO.md
git commit -m "Limpieza de texto: minúsculas, eliminación de puntuación y stopwords en español; integración en flujo de carga y guardado de frecuencias"
```

## Tokens y Nube de Palabras
- Se guardan **tokens procesados** (sin puntuación y sin stopwords) en `TextoAnalizado.tokens_json`.
- Se genera una **nube de palabras** por texto y se guarda como imagen en `TextoAnalizado.nube_imagen` (carpeta `media/wordclouds/`).

### Requisitos nuevos
Instala dependencias adicionales:
```bash
pip install -r requirements.txt
```

### Migraciones
Como se agregaron campos al modelo, ejecuta:
```bash
python manage.py makemigrations analisis
python manage.py migrate
```

### Commit sugerido
```bash
git add analisis/models.py analisis/views.py analisis/templates/analisis/lista.html requirements.txt README_CORRER_PROYECTO.md
git commit -m "Tokens procesados y nube de palabras: JSONField e ImageField en TextoAnalizado; generación tras la carga del archivo; plantilla actualizada"
```
>>>>>>> 76182a81822a6aa7a9c45c67f5f91222cbee9ddc
