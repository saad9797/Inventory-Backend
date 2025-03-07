# serializers.py
from rest_framework import serializers
from .models import User, Department  # Import your models
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    Password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['UserID', 'DepartmentID', 'Email', 'Role', 'Password']

    def create(self, validated_data):
        validated_data['Password'] = make_password(validated_data['Password'])
        user = User.objects.create(**validated_data)
        return user