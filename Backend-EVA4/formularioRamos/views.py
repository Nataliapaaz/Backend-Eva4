from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from formularioRamos.models import Ramos
from django.shortcuts import redirect
from .models import Ramos
from .serializers import RamoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def ramos_lista(request):
    if request.method == 'GET':
        ramos = Ramos.objects.all()
        serializer = RamoSerializer(ramos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = RamoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def ramos_detail(request, pk):
    try:
        ramos = Ramos.objects.get(pk=pk)
    except Ramos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RamoSerializer(ramos)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = RamoSerializer(ramos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        ramos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-____________

def home(request):
    return render(request, "index/home.html")


class RamosListaView(ListAPIView):
    queryset = Ramos.objects.all()
    serializer_class = RamoSerializer

class RamosDetalleView(RetrieveAPIView):
    queryset = Ramos.objects.all()
    serializer_class = RamoSerializer


"""
def renderTemplate(request):
   return render(request, "formularioRamos/formularioRamos.html")

def ramosData (request):
    ramos = Ramos.objects.all ()
    data = {'ramos' : ramos}
    return render (request, 'ramos/ramos.html', data)

def formulario_ramos(request):
    if request.method == 'POST':
        form = RamosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ramosData')
    else:
        form = RamosForm()

    return render(request, 'formularioramos/formularioramos.html', {'form': form})

def eliminar_ramo(request, idRamo):
    ramo = Ramos.objects.get(idRamo = idRamo)
    ramo.delete()
    return redirect('/ramos')

def modificar_ramos(request, idRamo):
    ramo = Ramos.objects.get(idRamo=idRamo)
    form = RamosForm(instance=ramo)

    if request.method == 'POST':
        form = RamosForm(request.POST, instance=ramo)
        if form.is_valid():
            form.save()
            return redirect('ramosData')

    data = {'form': form, 'modo': 'modificar', 'idRamo': idRamo}
    return render(request, 'formularioramos/formularioramosmod.html', data)

"""