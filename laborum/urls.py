from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('permisos/', include('permisos.urls')),
    path('catalogo_permisos/', include('catalogo_permisos.urls')),
    path('empleados/', include('empleados.urls')),
    path('puestos/', include('puestos.urls')),
    path('admin/', admin.site.urls),
]
