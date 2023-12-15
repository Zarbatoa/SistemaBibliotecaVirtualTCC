from django.db import models

class Livro(models.Model):
    titulo           = models.CharField(max_length=200)
    autor            = models.CharField(max_length=100)
    ano_publicacao   = models.IntegerField()
    descricao        = models.TextField(blank=True)
    isbn             = models.CharField(max_length=30)#max_length=13, unique=True)
    
    emprestado       = models.BooleanField(default=False)
    doado            = models.BooleanField(default=False)
    avaliacao        = models.FloatField()

    nome_pessoa_empr  = models.CharField(max_length=250, null=True, blank=True)
    data_emprest_doa  = models.DateField(null=True, blank=True) 



    def __str__(self):
        return str(self.pk) + "-" + self.titulo
    

class Usuario(models.Model):
    login = models.CharField(max_length=120, null=False, unique=True)
    senha = models.CharField(max_length=120, null=False)

    def __str__(self):
        return str(self.pk) + "-" + self.login

    

