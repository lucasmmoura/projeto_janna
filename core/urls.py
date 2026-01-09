from django.urls import path
from .views import home, campeao_detalhe

urlpatterns = [
    path('', home, name='home'),
    path('campeao/<int:id>/', campeao_detalhe, name='campeao_detalhe'),
]