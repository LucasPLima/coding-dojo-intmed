import imp

from django import urls
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CalculadoraViewSet

router = SimpleRouter()
router.register(
    "calculadoras", CalculadoraViewSet, "calculadora"
)
urlpatterns = [
    path('', include(router.urls))
]
    

