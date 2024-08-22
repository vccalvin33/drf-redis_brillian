from rest_framework import serializers
from .models import *

class InstituionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institutions
        fields = '__all__'