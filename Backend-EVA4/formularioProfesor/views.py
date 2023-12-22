from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Profesor
from .serializers import ProfesorSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins

# Create your views here.
class ProfesorLista(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
        
class ProfesorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


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
