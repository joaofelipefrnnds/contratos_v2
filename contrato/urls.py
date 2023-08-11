from django.urls import path, include
from contrato.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name='index'),
    path('cadastro_contrato/', cadastro_contrato, name='cadastro_contrato'),
    path('cadastro_empresa/', cadastro_empresa, name='cadastro_empresa'),
    path('cadastro_evento/', cadastro_evento, name='cadastro_evento'),
    path('listagem_evento/', listagem_evento, name='listagem_evento'),
    path('listagem_contrato/', listagem_contrato, name='listagem_contrato'),   
    path('listagem_empresa/', listagem_empresa, name='listagem_empresa'),
    path('listagem_empresa/', listagem_empresa, name='listagem_empresa'),
    path('detalhes_empresa/<int:empresa_id>', detalhes_empresa, name='detalhes_empresa'),
    path('detalhes_contrato/<int:contrato_id>', detalhes_contrato, name='detalhes_contrato'),
    path('detalhes_evento/<int:evento_id>', detalhes_evento, name='detalhes_evento'),
    path('update_contrato/<int:pk>', update_contrato, name='update_contrato'),
    path('update_evento/<int:pk>', update_evento, name='update_evento')
   # path('download/<int:pk>/', download, name='download'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
