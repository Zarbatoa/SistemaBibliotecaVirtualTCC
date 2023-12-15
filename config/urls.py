"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from livro.views import home_view, login_view, novo_livro_view, pesquisa_livro_view, \
    novo_usuario_view, pesquisa_usuario_view, dashboard_view, editar_usuario_view, editar_livro_view

urlpatterns = [
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),

    path('login/', login_view, name="login"),

    path('dashboard/', dashboard_view, name="dashboard"),
    path('novoLivro/', novo_livro_view, name="novo_livro"),
    path('pesquisaLivro/', pesquisa_livro_view, name="pesquisa_usuario"),
    path('novoUsuario/', novo_usuario_view, name="novo_usuario"),
    path('pesquisaUsuario/', pesquisa_usuario_view, name="pesquisa_livro"),

    path('editarUsuario/<int:id_usuario>', editar_usuario_view, name="editar_usuario"),
    path('editarLivro/<int:id_livro>', editar_livro_view, name="editar_livro"),

]
