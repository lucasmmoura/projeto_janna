from django.urls import path
from .views import home, campeao_detalhe
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('campeao/<slug:slug>/', campeao_detalhe, name='campeao_detalhe'),
    path('api/campeoes', views.api_campeoes, name='api_campeoes'),
    path('api/campeoes/<slug:slug>', views.api_campeao_detalhe, name='api_campeao_detalhe')
]