from django.contrib.auth import authenticate
from django.core.validators import EmailValidator
from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainSerializer


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[EmailValidator(message="Noto'gri email format."),
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="Bu email manzil allaqachon mavjud.")])

    username = serializers.CharField(validators=[UniqueValidator(
        queryset=User.objects.all(),
        message="Bu username allaqachon mavjud."
    )])

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio')


class CustomTokenObtainPairSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        self.username_field = 'email' if '@' in attrs.get('email', '') else 'username'

        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password']
        }

        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            raise serializers.ValidationError('Request context not found')

        user = authenticate(**authenticate_kwargs)

        if user is None or not user.is_active:
            raise serializers.ValidationError('No active account found with the given credentials')

        data = super().validate(attrs)

        return data

