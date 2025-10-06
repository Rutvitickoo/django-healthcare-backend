from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, Mapping

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '_all_'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '_all_'

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = '_all_'
