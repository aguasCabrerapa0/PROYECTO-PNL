from django import forms
from .models import TextoAnalizado

class TextoAnalizadoForm(forms.ModelForm):
<<<<<<< HEAD
    # Agregar campo para seleccionar n-grama
    TIPO_NGRAM_CHOICES = [
        (1, 'Unigramas (1-grama)'),
        (2, 'Bigramas (2-grama)'),
        (3, 'Trigramas (3-grama)'),
        (4, '4-grama'),
        (5, '5-grama'),
    ]
    
    tipo_ngram = forms.ChoiceField(
        choices=TIPO_NGRAM_CHOICES,
        initial=2,
        label="Tipo de n-grama",
        help_text="Selecciona el tipo de n-grama a calcular"
    )
    
    # Agregar checkbox para calcular probabilidades
    calcular_probabilidades = forms.BooleanField(
        required=False,
        initial=False,
        label="Calcular probabilidades MLE",
        help_text="Incluir cálculo de probabilidades condicionales con fronteras de oración"
    )
    
    class Meta:
        model = TextoAnalizado
        fields = ['titulo', 'archivo', 'tipo_ngram', 'calcular_probabilidades']
=======
    class Meta:
        model = TextoAnalizado
        fields = ['titulo', 'archivo']
        
>>>>>>> 76182a81822a6aa7a9c45c67f5f91222cbee9ddc
