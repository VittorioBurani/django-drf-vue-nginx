from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from custom.password_validators import NumberValidator, UppercaseValidator, SymbolValidator
from accounts.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        token['password_reset_required'] = user.password_reset_required
        return token


class UserDisplaySerializer(serializers.ModelSerializer):
    '''Generic User Serializer'''
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "is_staff", "is_superuser"]


class PasswordResetSerializer(serializers.Serializer):
    '''Password Reset Serializer'''
    new_password = serializers.CharField(min_length=8, write_only=True, validators=(NumberValidator().validate, UppercaseValidator().validate, SymbolValidator().validate))
    confirm_password = serializers.CharField(min_length=8, write_only=True, validators=(NumberValidator().validate, UppercaseValidator().validate, SymbolValidator().validate))
