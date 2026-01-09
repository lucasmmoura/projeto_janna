from django.urls import path
from .views import home, camepao_detalhe

urlpatterns = [
    path('', home, name='home'),
    path('campeao/<int:id>/', camepao_detalhe, name='campeao_detalhe'),
]