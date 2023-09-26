from django.urls import path
from e_commerce.api.hola_mundo_api import *
from e_commerce.api.marvel_api_views import *

urlpatterns = [
    path('holamundo/',hola_mundo),
    path('request-nombre/', return_request_nombre),
    path('request-objetivo/', return_request_objetivo),
    path('get-comics/',get_comics),
    path('purchased-item/',purchased_item),
]