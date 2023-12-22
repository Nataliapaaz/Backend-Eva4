from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from formularioRamos.models import Ramos
from django.shortcuts import redirect
from .models import Ramos
from .serializers import RamoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins


# Create your views here.
class RamoLista(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Ramos.objects.all()
    serializer_class = RamoSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
        
class RamoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Ramos.objects.all()
    serializer_class = RamoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)



# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-____________

def home(request):
    return render(request, "index/home.html")


class RamosListaView(ListAPIView):
    queryset = Ramos.objects.all()
    serializer_class = RamoSerializer

class RamosDetalleView(RetrieveAPIView):
    queryset = Ramos.objects.all()
    serializer_class = RamoSerializer
