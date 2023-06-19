from django.urls import path
from usuarios.views import login, cadastro_usuario, listagem_usuario, logout

urlpatterns = [
   path('listagem_usuario', listagem_usuario, name='listagem_usuario'),
   path('cadastro_usuario', cadastro_usuario, name='cadastro_usuario'),
   path('login', login, name='login'),
   path('logout', logout, name='logout'),
    
]
