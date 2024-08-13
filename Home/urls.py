from rest_framework import routers

from Home.views import EmpleadoViewSet, MarcaViewSet, UnidadadministrativaViewSet, AreaViewSet, EquipoViewSet
from RestFullAPI import settings

router = routers.DefaultRouter()

router.register(settings.API_PREFIX_STRING+'/empleados', EmpleadoViewSet,'empleados')
router.register(settings.API_PREFIX_STRING+'/marcas', MarcaViewSet,'marcas')
router.register(settings.API_PREFIX_STRING+'/unidades-administrativas', UnidadadministrativaViewSet,'unidades-administrativas')
router.register(settings.API_PREFIX_STRING+'/areas', AreaViewSet,'areas')
router.register(settings.API_PREFIX_STRING+'/equipos', EquipoViewSet,'equipos')


urlpatterns = router.urls

