from django.contrib import admin
from django.urls import path, include

from configuracao import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
    path('accounts/', include('usuarios.urls')),
    path('minhas_receitas/', include('crud_receitas.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
