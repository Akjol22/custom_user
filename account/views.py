from django.shortcuts import render
from rest_framework.views import APIView

from .permissions import IsActivePermission
from .serializers import RegistrationSerializer, LoginSerializer, ActivationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Аккаунт успешно создан', status=201)


class ActivationView(APIView):
    def post(self, request):
        serilizer = ActivationSerializer(
            data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.activate()
        return Response('Аккаунт успешно активирован', status=200)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = [IsActivePermission]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response(
            'Вы вышли со своего аккаунта'
        )
