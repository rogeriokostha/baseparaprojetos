from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .serializers import RegisterSerializer, MeSerializer, LogoutSerializer 

@extend_schema_view(
    post=extend_schema(
        tags=["Auth"],
        summary="Login",
        description="Autentica o usuário e retorna os tokens access e refresh."
    )
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(
        tags=["Auth"],
        summary="Renovar token",
        description="Recebe um refresh token válido e retorna um novo access token."
    )
)
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema_view(
    post=extend_schema(
        tags=["Auth"],
        summary="Verificar token",
        description="Valida se um token informado ainda é válido."
    )
)
class CustomTokenVerifyView(TokenVerifyView):
    pass


@extend_schema_view(
    post=extend_schema(
        tags=["Auth"],
        summary="Cadastrar usuário",
        description="Cria um novo usuário no sistema.",
    )
)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MeSerializer

    @extend_schema(
        tags=["Auth"],
        summary="Usuário logado",
        description="Retorna os dados do usuário autenticado.",
        responses=MeSerializer,
    )
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LogoutSerializer

    @extend_schema(
        tags=["Auth"],
        summary="Logout",
        description="Invalida o refresh token enviado, encerrando a sessão do usuário.",
        request=LogoutSerializer,
        responses={205: None},
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data["refresh"]

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            raise ValidationError({"refresh": "Token inválido ou expirado."})

        return Response(
            {"detail": "Logout realizado com sucesso."},
            status=status.HTTP_205_RESET_CONTENT,
        )