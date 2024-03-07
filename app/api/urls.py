from rest_framework.routers import DefaultRouter
from .viewsets import ViaCepViewset
from django.urls import path, include

router = DefaultRouter()

router.register(basename="cep",viewset=ViaCepViewset, prefix="cep")

urlpatterns = [

    path("api/", include(router.urls))

]