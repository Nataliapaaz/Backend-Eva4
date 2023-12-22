from rest_framework import serializers
from formularioRamos.models import Ramos

class RamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ramos
        fields = '__all__'