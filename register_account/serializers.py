from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Register User db
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length = 8)


    class Meta :
        model = User
        fields = ['id', 'username', 'email' ,'password', 'phone']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email Alreay Exists')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password'],
            phone= validated_data['phone']
        )
        return user

# LOGIN Serializer
class LoginSerializer (serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
           user =  User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid Email or Password')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid Invalid or Password')

        if not user.is_active:
            raise serializers.ValidationError('User is not active')

        data ['user'] = user

        return data
                                  