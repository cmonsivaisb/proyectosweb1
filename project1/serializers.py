from rest_framework import serializers
from project1.models import Proyecto
from django.contrib.auth.models import User

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')

    def get_role(self, obj):
        # Define cómo determinar el rol del usuario aquí.
        # Puedes usar obj.is_staff o cualquier otra lógica que necesites.
        if obj.is_staff:
            return 'admin'
        else:
            return 'visor'
