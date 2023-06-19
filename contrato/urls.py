from django.urls import path, include
from contrato.views import index, cadastro_contrato, cadastro_empresa, cadastro_evento, listagem_empresa, listagem_contrato, detalhes_empresa
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name='index'),
    path('cadastro_contrato/', cadastro_contrato, name='cadastro_contrato'),
    path('cadastro_empresa/', cadastro_empresa, name='cadastro_empresa'),
    path('cadastro_evento/', cadastro_evento, name='cadastro_evento'),
    path('listagem_contrato/', listagem_contrato, name='listagem_contrato'),   
    path('listagem_empresa/', listagem_empresa, name='listagem_empresa'),
    path('listagem_empresa/', listagem_empresa, name='listagem_empresa'),
    path('detalhes_empresa/<int:empresa_id>', detalhes_empresa, name='detalhes_empresa'),
    
    
] + static(settings.MEDIA_URL, documento_root=settings.MEDIA_ROOT)
