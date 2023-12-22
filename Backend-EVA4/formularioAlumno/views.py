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
from rest_framework import generics, mixins

# Create your views here.
class AlumnoLista(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
        
class AlumnoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)



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

