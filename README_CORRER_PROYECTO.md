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