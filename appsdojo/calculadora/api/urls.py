from django.urls import include, path
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter

from .views import CalculadoraViewSet, VariavelCalculadoraViewSet

router = SimpleRouter()
router.register(
    "calculadoras", CalculadoraViewSet, "calculadora"
)
variavel_router=NestedSimpleRouter(router, 'calculadoras', lookup='calculadora')
variavel_router.register(
    'variaveis', VariavelCalculadoraViewSet, basename='variavel'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(variavel_router.urls))
]
    

