from django.db import router
from rest_framework import urlpatterns
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reservas', ReservaViewsets)
router.register(r'chaves', ChaveViewsets)
router.register(r'pessoas', PessoaViewsets)

urlpatterns = router.urls