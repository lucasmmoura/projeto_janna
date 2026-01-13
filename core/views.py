from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Campeao
# Create your views here.


def home(request):
    campeoes = Campeao.objects.all()
    return render(request, 'core/home.html', {
        'campeoes': campeoes
    })

def campeao_detalhe(request, slug):
    campeao = get_object_or_404(Campeao, slug=slug) #Busca no banco um campeão com o id igual ao da url; Se achar retorna o objeto, se não achar = pagina 404
    return render(request, "core/campeao_detalhe.html", # Template
                  {
        "campeao": campeao #Objeto para o template
    })

def api_campeoes(request):
    campeoes = Campeao.objects.all()

    data = []
    for campeao in campeoes:
        data.append({
            "nome": campeao.nome,
            "funcao": campeao.funcao,
            "descricao": campeao.descricao,
            "slug": campeao.slug,
        })

    return JsonResponse(data, safe=False)


def api_campeao_detalhe(request, slug):
    campeao = get_object_or_404(Campeao, slug=slug)

    data = {
        "nome": campeao.nome,
        "funcao": campeao.funcao,
        "descricao": campeao.descricao,
        "slug": campeao.slug,
    }

    return JsonResponse(data)