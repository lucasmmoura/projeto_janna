from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Campeao
# Create your views here.


def home(request):
    campeoes = Campeao.objects.all()
    return render(request, 'core/home.html', {
        'campeoes': campeoes
    })

def campeao_detalhe(request, id):
    campeao = get_object_or_404(Campeao, id=id) #Busca no banco um campeão com o id igual ao da url; Se achar retorna o objeto, se não achar = pagina 404
    return render(request, "core/campeao_detalhe_html", # Template
                  {
        "campeao": campeao #Objeto para o template
    })
