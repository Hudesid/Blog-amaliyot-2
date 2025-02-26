from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import transaction
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import User, UserToken
from django.contrib.auth import settings


class AuthorValidate(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class SingUpCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = UserToken.objects.create(user=user)
            verification_link = reverse("verify-email", kwargs={'pk': user.id, 'token': token.token})
            current_site = get_current_site(request).domain
            full_link = f"http://{current_site}{verification_link}"
            message = f"Sizning akountizdan Blog saytidan ro'yxatdan o'tildi.\\Blog saytiga o'tish uchun bu link orqali o'tshingiz mumkin: {full_link}"
            try:
                send_mail(
                    'Blog saytidan habar',
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False
                )
            except Exception as e:
                return Response({'message': "Emailga habar jo'natishda muomo paydo bo'ldi."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'message': f"{user.username} ismli foydalunuvchi ro'yxatdan o'tdi."
            }, status=status.HTTP_201_CREATED)


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class VerifyEmailAPIView(APIView):
    def get(self, request, pk=None, token=None):
        if not pk:
            raise ValueError('ID necessary')
        if not token:
            raise ValueError('Token necessary')
        try:
            user = User.objects.get(id=pk)
            token = UserToken.objects.get(token=token)
        except User.DoesNotExist:
            return Response({'message': 'The user ID is wrong'}, status=status.HTTP_400_BAD_REQUEST)
        except UserToken.DoesNotExist:
            return Response({'message': 'The user token is wrong'}, status=status.HTTP_400_BAD_REQUEST)

        if token.expires <= timezone.now() and not user.is_verify_email:
            with transaction.atomic():
                token.delete()
                user.delete()
            return Response({'message': 'Token has expired and user is deleted'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_verify_email = True
        user.is_active = True
        user.save()
        token.delete()

        return Response({'message': 'Token verified successfully'}, status=status.HTTP_200_OK)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, AuthorValidate]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = UserToken.objects.create(user=user)
            verification_link = reverse("verify-email", kwargs={'pk': user.id, 'token': token.token})
            current_site = get_current_site(request).domain
            full_link = f"http://{current_site}{verification_link}"
            message = f"Emailgizni tasdiqlash uchun shu link bo'yicha Blog saytiga o'ting: {full_link}."
            try:
                send_mail(
                    'Blog saytidan habar',
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False
                )
            except Exception as e:
                return Response({'message': "Emailga habar jo'natishda muomo paydo bo'ldi."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'message': f"{user.username} ismli foydalunuvchi profile yangilandi."
            }, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



