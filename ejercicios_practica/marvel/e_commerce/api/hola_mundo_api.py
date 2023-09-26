# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view,  permission_classes

# Primera vista con método GET.
#@api_view(['GET'])
def hola_mundo(request):
    template = '<h1>¡Hola Mundo! Esto es Django APIs.</h1>' 
    return HttpResponse(template)

# Segunda vista con métodos GET y POST.
#@api_view(['GET', 'POST'])
#@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def return_request_nombre(request):
    '''
    Esta función nos permite realizar una petición de tipo POST,
    \n Retorna el valor del parámetro "mi_nombre" enviada en la petición.
    '''
    template = f'<h1>Bienvenido: {request.GET.get("mi_nombre")}</h1>'
    print(template)
    return HttpResponse(template)

# Tercera vista con métodos GET y POST.
#@api_view(['GET', 'POST'])
#@permission_classes([]) # Eliminamos la necesidad de autenticar al usuario.
def return_request_objetivo(request):
    '''
    Esta función nos permite realizar una petición de tipo POST,
    \n Retorna el valor del parámetro "mi_nombre" enviada en la petición.
    '''
    template = f'<h1>Práctica clase 4 realizada por {request.GET.get("mi_nombre")}</h1>'
    print(template)
    return HttpResponse(template)
