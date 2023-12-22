from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Alumno
from .serializers import AlumnoSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class AlumnoLista(APIView):

    def get(self, request):
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AlumnoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class AlumnoDetail(APIView):
    def get_object(self, pk):
        try:
            return AlumnoDetail.objects.get(pk=pk)
        except AlumnoDetail.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        alumno = self.get_object(pk)
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)
    
    def put(self, request, pk):
        alumno = self.get_object(pk)
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        alumno = self.get_object(pk)
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
@api_view(['GET', 'POST'])
def alumno_lista(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AlumnoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def alumno_detail(request, pk):
    try:
        alumnos = Alumno.objects.get(pk=pk)
    except Alumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AlumnoSerializer(alumnos)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = AlumnoSerializer(alumnos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        alumnos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-____________
def home(request):
    return render(request, "index/home.html")

def alumnoView(request):  
    alumnos = Alumno.objects.all()
    data = {'alumnos': list(alumnos.values('nombre', 'apellido'))}  
    return JsonResponse(data)

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-____________

class AlumnoListaView(ListAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoDetalleView(RetrieveAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

