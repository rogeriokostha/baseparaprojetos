from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, ProfileSerializer
from rest_framework import generics




@extend_schema_view(
    list=extend_schema(
        tags=["Usuários"],
        summary="Listar usuários",
        description="Retorna a lista de usuários cadastrados no sistema."
    ),
    retrieve=extend_schema(
        tags=["Usuários"],
        summary="Detalhar usuário",
        description="Retorna os dados completos de um usuário específico."
    ),
    create=extend_schema(
        tags=["Usuários"],
        summary="Criar usuário",
        description="Cria um novo usuário no sistema."
    ),
    update=extend_schema(
        tags=["Usuários"],
        summary="Atualizar usuário",
        description="Atualiza todos os dados de um usuário existente."
    ),
    partial_update=extend_schema(
        tags=["Usuários"],
        summary="Atualizar parcialmente usuário",
        description="Atualiza apenas alguns campos de um usuário."
    ),
    destroy=extend_schema(
        tags=["Usuários"],
        summary="Excluir usuário",
        description="Remove um usuário do sistema."
    ),
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]




@extend_schema_view(
    get=extend_schema(
        tags=["Perfil"],
        summary="Consultar perfil",
        description="Retorna os dados do usuário autenticado."
    ),
    put=extend_schema(
        tags=["Perfil"],
        summary="Atualizar perfil",
        description="Atualiza todos os dados do perfil do usuário autenticado."
    ),
    patch=extend_schema(
        tags=["Perfil"],
        summary="Atualizar parcialmente perfil",
        description="Atualiza apenas alguns campos do perfil do usuário autenticado."
    ),
)
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

