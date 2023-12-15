from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LivroForm, RawLivroForm, RawUsuarioForm
from .models import Livro, Usuario


# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
    # Ver como resolver isto: Assumo que vem pelo link de logou do dashboard
    request.session['usuario_login'] = None

    form = RawUsuarioForm()
    if request.method == "POST":
        form = RawUsuarioForm(request.POST)
        if form.is_valid():
            usuario = Usuario.objects.filter(login__exact=request.POST.get("login"))
            if len(usuario) > 0 and usuario[0].senha == request.POST.get("senha"):
                request.session['usuario_login'] = usuario[0].login
                print ("logado!!!")
                return redirect('../dashboard/',)
    
    context = {
        "form": form
    }

    return render(request, "login.html", context)

#tela pos-login:
def dashboard_view(request, *args, **kwargs):
    usuario_login = request.session['usuario_login']
    context = {
        "usuario_login": usuario_login
    }
    return render(request, "dashboard.html", context)



def novo_livro_view(request, *args, **kwargs):
    # form = LivroForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = LivroForm()
    form = RawLivroForm()
    if request.method == "POST":
        form = RawLivroForm(request.POST)
        if form.is_valid():
            Livro.objects.create(**form.cleaned_data)
            form = RawLivroForm()
    
    context = {
        'form': form
    }
    return render(request, "novoLivro.html", context)


def editar_livro_view(request, id_livro, *args, **kwargs):
    livro = get_object_or_404(Livro, pk=id_livro)
    print(livro)
    form = RawLivroForm({
        "titulo": livro.titulo,
        "autor": livro.autor,
        "ano_publicacao":livro.ano_publicacao,
        "descricao": livro.descricao,
        "isbn": livro.isbn,

        "emprestado": livro.emprestado,
        "doado": livro.doado,
        "avaliacao": livro.avaliacao,
        "nome_pessoa_empr": livro.nome_pessoa_empr,
        "data_emprest_doa": livro.data_emprest_doa
    })
    if request.method == "POST":
        form = RawLivroForm(request.POST)
        if form.is_valid():
            livro.titulo           = form.cleaned_data["titulo"]
            livro.autor            = form.cleaned_data["autor"]
            livro.ano_publicacao   = form.cleaned_data["ano_publicacao"]
            livro.descricao        = form.cleaned_data["descricao"]
            livro.isbn             = form.cleaned_data["isbn"]

            livro.emprestado       = form.cleaned_data["emprestado"]
            livro.doado            = form.cleaned_data["doado"]
            livro.avaliacao        = form.cleaned_data["avaliacao"]
            livro.nome_pessoa_empr = form.cleaned_data["nome_pessoa_empr"]
            livro.data_emprest_doa = form.cleaned_data["data_emprest_doa"]
            livro.save()
            return redirect('../pesquisaLivro/')
    
    context = {
        'form': form
    }
    return render(request, "editarLivro.html", context)


def pesquisa_livro_view(request, *args, **kwargs):
    objs = []
    if request.method == "POST":
        if 'Pesquisar' in request.POST.get('acao'):
            if(request.POST.get('texto_pesquisa') == ""):
                objs = Livro.objects.all()
            else:
                objs = Livro.objects.filter(titulo__startswith=request.POST.get('texto_pesquisa'))
        elif 'Limpar' in request.POST.get('acao'):
            objs = []

    context = {
        'livros': objs
    }
    return render(request, "pesquisaLivro.html", context)


def novo_usuario_view(request, *args, **kwargs):
    form = RawUsuarioForm()
    if request.method == "POST":
        form = RawUsuarioForm(request.POST)
        if form.is_valid():
            Usuario.objects.create(**form.cleaned_data)
            form = RawUsuarioForm()
    
    context = {
        "form": form
    }

    return render(request, "novoUsuario.html", context)

def editar_usuario_view(request, id_usuario, *args, **kwargs):
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    print(usuario)
    form = RawUsuarioForm({"login":usuario.login, "senha": usuario.senha})
    if request.method == "POST":
        form = RawUsuarioForm(request.POST)
        if form.is_valid():
            #o login nao serah alterado!
            usuario.senha = form.cleaned_data["senha"]
            usuario.save()
            return redirect('../pesquisaUsuario/')
    
    context = {
        "form": form
    }

    return render(request, "editarUsuario.html", context)

def pesquisa_usuario_view(request, *args, **kwargs):
    objs = []
    if request.method == "POST":
        if 'Pesquisar' in request.POST.get('acao'):
            if(request.POST.get('texto_pesquisa') == ""):
                objs = Usuario.objects.all()
            else:
                objs = Usuario.objects.filter(login__startswith=request.POST.get('texto_pesquisa'))
        elif 'Limpar' in request.POST.get('acao'):
            objs = []



    context = {
        'usuarios': objs
    }
    return render(request, "pesquisaUsuario.html", context)
