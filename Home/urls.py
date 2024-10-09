from rest_framework import routers

from Home.views import EmpleadoViewSet, MarcaViewSet, UnidadadministrativaViewSet, AreaViewSet, EquipoViewSet, \
    EquipoFullViewSet, UnidadadministrativaFullViewSet, SubareaViewSet, CategoriaDeEquipoViewSet, ModeloViewSet, \
    ColorViewSet, CondicionViewSet, FuenteDeFinanciamientoViewSet
from Servicios.views import TicketFullViewSet, TicketViewSet, TicketImagenFullViewSet, TicketImagenViewSet, \
    TicketRespuestaFullViewSet, TicketRespuestaViewSet, TicketRespuestaImagenFullViewSet, TicketRespuestaImagenViewSet

from RestFullAPI import settings

router = routers.DefaultRouter()

router.register(settings.API_PREFIX_STRING+'/empleados', EmpleadoViewSet,'empleados')
router.register(settings.API_PREFIX_STRING+'/marcas', MarcaViewSet,'marcas')
router.register(settings.API_PREFIX_STRING+'/unidades-administrativas-full', UnidadadministrativaFullViewSet,'unidades-administrativas-full')
router.register(settings.API_PREFIX_STRING+'/unidades-administrativas', UnidadadministrativaViewSet,'unidades-administrativas')
router.register(settings.API_PREFIX_STRING+'/equipos-full', EquipoFullViewSet,'equipos-full')
router.register(settings.API_PREFIX_STRING+'/equipos', EquipoViewSet,'equipos')
router.register(settings.API_PREFIX_STRING+'/areas', AreaViewSet,'areas')
router.register(settings.API_PREFIX_STRING+'/subareas', SubareaViewSet,'subareas')
router.register(settings.API_PREFIX_STRING+'/categoria-de-equipos', CategoriaDeEquipoViewSet,'categoria-de-equipos')
router.register(settings.API_PREFIX_STRING+'/modelos', ModeloViewSet,'modelos')
router.register(settings.API_PREFIX_STRING+'/colores', ColorViewSet,'colores')
router.register(settings.API_PREFIX_STRING+'/condiciones-de-equipos', CondicionViewSet,'condiciones-de-equipos')
router.register(settings.API_PREFIX_STRING+'/fuentes-de-finaciamiento', FuenteDeFinanciamientoViewSet,'fuentes-de-finaciamiento')

router.register(settings.API_PREFIX_STRING+'/tickets-full', TicketFullViewSet,'tickets-full')
router.register(settings.API_PREFIX_STRING+'/tickets', TicketViewSet,'tickets')
router.register(settings.API_PREFIX_STRING+'/tickets-imagen-full', TicketImagenFullViewSet,'tickets-imagen-full')
router.register(settings.API_PREFIX_STRING+'/tickets-imagen', TicketImagenViewSet,'tickets-imagen')
router.register(settings.API_PREFIX_STRING+'/tickets-respuesta-full', TicketRespuestaFullViewSet,'tickets-respuesta-full')
router.register(settings.API_PREFIX_STRING+'/tickets-respuesta', TicketRespuestaViewSet,'tickets-respuesta')
router.register(settings.API_PREFIX_STRING+'/tickets-respuesta-imagen-full', TicketRespuestaImagenFullViewSet,'tickets-respuesta-imagen-full')
router.register(settings.API_PREFIX_STRING+'/tickets-respuesta-imagen', TicketRespuestaImagenViewSet,'tickets-respuesta-imagen')

urlpatterns = router.urls

