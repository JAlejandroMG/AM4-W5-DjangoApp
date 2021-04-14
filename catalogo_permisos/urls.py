from rest_framework.routers import DefaultRouter

from catalogo_permisos.views import CatalogoPermisosViewSet

router = DefaultRouter()
router.register('', CatalogoPermisosViewSet)

urlpatterns = router.urls
