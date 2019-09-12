from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # 모델 설정
        fields = ('username','first_name','password') # 필드 설정
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],None,validated_data['password'],first_name=validated_data['first_name']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username', 'first_name')

class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('unable to login with provided credentials')
