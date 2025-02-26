from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True)
    
    class Meta:
        model=User
        fields=['username','email','password']
        
    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model:User
        fields=['id','username','email']