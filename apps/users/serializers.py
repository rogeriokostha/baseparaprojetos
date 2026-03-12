from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    nome_completo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "nome_completo",
        ]
        read_only_fields = [
            "id",
            "nome_completo",
        ]

    def get_nome_completo(self, obj) -> str:
        return obj.nome_completo

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    nome_completo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "nome_completo",
            "telefone",
            "telefone_whatsapp",
            "genero",
            "membership_type",
            "cidade",
            "estado",
            "pais",
            "avatar",
            "bio",
            "website",
            "receber_newsletter",
            "date_joined",
            "is_active",
            "is_staff",
        ]
        read_only_fields = [
            "id",
            "date_joined",
            "is_active",
            "is_staff",
        ]

    def get_nome_completo(self, obj) -> str:
        return obj.nome_completo


class ProfileSerializer(serializers.ModelSerializer):
    nome_completo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "nome_completo",
            "telefone",
            "telefone_whatsapp",
            "data_nascimento",
            "genero",
            "avatar",
            "bio",
            "website",
            "cidade",
            "estado",
            "pais",
            "idioma",
            "timezone",
            "receber_newsletter",
            "membership_type",
        ]
        read_only_fields = [
            "id",
            "email",
            "membership_type",
        ]

    def get_nome_completo(self, obj) -> str:
        return obj.nome_completo

class MeSerializer(serializers.ModelSerializer):
    nome_completo = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "nome_completo",
            "is_staff",
        ]

    def get_nome_completo(self, obj) -> str:
        return obj.nome_completo


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()