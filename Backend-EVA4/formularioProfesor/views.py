from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Profesor
from .serializers import ProfesorSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class ProfesorLista(APIView):

    def get(self, request):
        profesores = Profesor.objects.all()
        serializer = ProfesorSerializer(profesores, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfesorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProfesorDetail(APIView):
    def get_object(self, pk):
        try:
            return Profesor.objects.get(pk=pk)
        except Profesor.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        profesor = self.get_object(pk)
        serializer = ProfesorSerializer(profesor)
        return Response(serializer.data)
    
    def put(self, request, pk):
        profesor = self.get_object(pk)
        serializer = ProfesorSerializer(profesor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        profesor = self.get_object(pk)
        profesor.delete()
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
