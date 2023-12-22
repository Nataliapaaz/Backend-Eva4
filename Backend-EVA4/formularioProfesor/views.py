from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Profesor
from .serializers import ProfesorSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def profesor_lista(request):
    print("Entro a la vista de Alumnos")
    if request.method == 'GET':
        profesores = Profesor.objects.all()
        serializer = ProfesorSerializer(profesores, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProfesorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def profesor_detail(request, pk):
    try:
        profesores = Profesor.objects.get(pk=pk)
    except Profesor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfesorSerializer(profesores)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ProfesorSerializer(profesores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        profesores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def profesorView(request):  
    profesores = Profesor.objects.all()
    data = {'profesor': list(profesores.values('nombre', 'apellido'))}  
    return JsonResponse(data)

class ProfesorListaView(ListAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class ProfesorDetalleView(RetrieveAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
