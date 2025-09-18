
import re
from collections import Counter

STOPWORDS = set(['a', 'ademas', 'ademas,', 'al', 'algo', 'algunas', 'algunos', 'ante', 'antes', 'aunque', 'aún', 'bajo', 'cabe', 'cada', 'cierto', 'como', 'con', 'contra', 'cual', 'cuales', 'cuando', 'cuanta', 'cuantas', 'cuanto', 'cuantos', 'cuál', 'cuáles', 'cuán', 'cómo', 'de', 'del', 'desde', 'donde', 'dos', 'dónde', 'el', 'ella', 'ellas', 'ellos', 'en', 'entre', 'era', 'erais', 'eramos', 'eran', 'eres', 'es', 'esa', 'esas', 'ese', 'esos', 'esta', 'estaban', 'estamos', 'estan', 'estaría', 'estarían', 'estas', 'este', 'esto', 'estos', 'estoy', 'está', 'estábamos', 'están', 'estás', 'fue', 'fueron', 'fui', 'fuimos', 'fuiste', 'ha', 'habido', 'había', 'habíamos', 'habían', 'hace', 'haceis', 'hacemos', 'hacen', 'hacer', 'hacia', 'haciendo', 'han', 'hasta', 'hay', 'hicieron', 'hizo', 'incluso', 'jamás', 'junto', 'la', 'larga', 'largas', 'largo', 'largos', 'las', 'le', 'les', 'lo', 'los', 'mas', 'me', 'mi', 'mia', 'mias', 'mio', 'mios', 'mis', 'mucha', 'muchas', 'mucho', 'muchos', 'muy', 'nada', 'ni', 'ninguna', 'ningunas', 'ninguno', 'ningunos', 'no', 'nos', 'nosotras', 'nosotros', 'nunca', 'o', 'os', 'otra', 'otras', 'otro', 'otros', 'para', 'pero', 'poca', 'pocas', 'poco', 'pocos', 'por', 'porque', 'posiblemente', 'primer', 'primera', 'primeras', 'primeros', 'propia', 'propias', 'propio', 'propios', 'que', 'quien', 'quienes', 'qué', 'se', 'según', 'ser', 'si', 'siendo', 'sin', 'sino', 'sobre', 'solamente', 'solo', 'somos', 'soy', 'sr', 'sra', 'sres', 'su', 'sus', 'suya', 'suyas', 'suyo', 'suyos', 'sí', 'sólo', 'tal', 'tales', 'también', 'tampoco', 'tan', 'tanto', 'te', 'tendremos', 'tendrá', 'tendrán', 'teneis', 'tenemos', 'tengo', 'tiene', 'tienen', 'tienes', 'toda', 'todas', 'todo', 'todos', 'tras', 'tu', 'tus', 'tuya', 'tuyas', 'tuyo', 'tuyos', 'un', 'una', 'unas', 'uno', 'unos', 'usted', 'ustedes', 'vais', 'vamos', 'van', 'vosotros', 'voy', 'vuestra', 'vuestras', 'vuestro', 'vuestros', 'y', 'ya', 'yo', 'él', 'ésa', 'ésas', 'ése', 'ésos'])

def tokenize_spanish(text: str):
    """Tokeniza extrayendo solo letras (incluye acentos/ñ)."""
    text = text.lower()
    # Mantener letras (incluyendo acentos y ñ), separar todo lo demás
    tokens = re.findall(r"[a-záéíóúüñ]+", text, flags=re.IGNORECASE)
    return tokens

def clean_and_filter(text: str):
    """
    Convierte a minúsculas, elimina signos de puntuación implícitamente
    al quedarnos solo con letras, y filtra stopwords en español.
    Devuelve la lista de tokens limpios.
    """
    tokens = tokenize_spanish(text)
    filtered = [t for t in tokens if t not in STOPWORDS and len(t) > 0]
    return filtered

def frequencies(tokens):
    return Counter(tokens)
<<<<<<< HEAD


def ngram_frequencies(tokens, n=2):
    """
    Devuelve un Counter con las frecuencias de n-gramas
    a partir de una lista de tokens.
    """
    if n < 2:
        return Counter()  # si n=1 ya usamos frequencies normales
    ngrams = zip(*[tokens[i:] for i in range(n)])
    joined = [' '.join(gram) for gram in ngrams]
    return Counter(joined)
=======
>>>>>>> 76182a81822a6aa7a9c45c67f5f91222cbee9ddc
