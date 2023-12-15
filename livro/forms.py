
from django import forms

from .models import Livro, Usuario

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo',
            'autor',
            'ano_publicacao',
            'descricao',
            'isbn',

            'emprestado',
            'doado',
            'avaliacao',

            'nome_pessoa_empr',
            'data_emprest_doa',
        ]


# Logo mais faço ester raw form
class RawLivroForm(forms.Form):
    titulo           = forms.CharField(label="Título:")
    autor            = forms.CharField()
    ano_publicacao   = forms.IntegerField(label="Ano de publicação:")
    descricao        = forms.CharField(label="Descrição:", widget=forms.Textarea(attrs={"rows":5}))
    isbn             = forms.CharField(label="ISBN:")

    emprestado       = forms.BooleanField(required=False)
    doado            = forms.BooleanField(required=False)
    avaliacao        = forms.FloatField()

    nome_pessoa_empr = forms.CharField(label="Nome da pessoa do empréstimo/doação:", required=False)
    data_emprest_doa = forms.DateField(label="Data do empréstimo/doação:", required=False)


class RawUsuarioForm(forms.Form):
    login = forms.CharField()
    senha = forms.CharField()
    
