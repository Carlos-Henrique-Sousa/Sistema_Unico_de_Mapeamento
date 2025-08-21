from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class LoginSerilizer(serializers.Serializer):
    identifier = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        user = authenticate(username=data['identifier'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Identificador ou senha inválidos.")
        data['user'] = user
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'identifier',
            'email',
            'nome',
            'type',
            'metadata'
        ]
        read_only_fields = ['id', 'is_active', 'is_staff', 'is_superuser']