from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html, mark_safe

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = (
        "avatar_preview",
        "email",
        "nome_completo_admin",
        "membership_badge",
        "is_staff",
        "is_active",
        "date_joined",
    )

    list_display_links = (
        "email",
        "nome_completo_admin",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "membership_type",
        "genero",
        "idioma",
        "telefone_whatsapp",
        "receber_newsletter",
        "terms_accepted",
        "date_joined",
    )

    search_fields = (
        "email",
        "first_name",
        "last_name",
        "telefone",
        "cpf_cnpj",
        "cidade",
        "estado",
        "pais",
    )

    ordering = ("-date_joined",)

    readonly_fields = (
        "avatar_preview_large",
        "date_joined",
        "last_login",
        "data_terms_accepted",
    )

    fieldsets = (
        ("Acesso", {
            "fields": (
                "email",
                "password",
            )
        }),
        ("Perfil", {
            "fields": (
                "avatar_preview_large",
                "avatar",
                "first_name",
                "last_name",
                "bio",
                "website",
            )
        }),
        ("Informações pessoais", {
            "fields": (
                "telefone",
                "telefone_whatsapp",
                "data_nascimento",
                "genero",
                "cpf_cnpj",
            )
        }),
        ("Localização", {
            "fields": (
                "cidade",
                "estado",
                "pais",
                "latitude",
                "longitude",
                "timezone",
                "idioma",
            )
        }),
        ("Plano e preferências", {
            "fields": (
                "membership_type",
                "receber_newsletter",
                "rede_social",
                "metadata",
            )
        }),
        ("Termos", {
            "fields": (
                "terms_accepted",
                "data_terms_accepted",
            )
        }),
        ("Permissões", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Datas importantes", {
            "fields": (
                "last_login",
                "date_joined",
            )
        }),
    )

    add_fieldsets = (
        ("Criar novo usuário", {
            "classes": ("wide",),
            "fields": (
                "email",
                "first_name",
                "last_name",
                "password1",
                "password2",
                "is_staff",
                "is_active",
            ),
        }),
    )

    def nome_completo_admin(self, obj):
        return obj.nome_completo or "-"
    nome_completo_admin.short_description = "Nome"

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="36" height="36" style="border-radius:50%; object-fit:cover; border:1px solid #d1d5db;" />',
                obj.avatar.url
            )
        return mark_safe(
            '<div style="width:36px; height:36px; border-radius:50%; background:#e5e7eb; display:flex; align-items:center; justify-content:center; font-size:12px; color:#374151;">-</div>'
        )
    avatar_preview.short_description = "Avatar"

    def avatar_preview_large(self, obj):
        if obj and obj.avatar:
            return format_html(
                '<img src="{}" width="80" height="80" style="border-radius:50%; object-fit:cover; border:2px solid #d1d5db;" />',
                obj.avatar.url
            )
        return "Sem avatar"
    avatar_preview_large.short_description = "Preview do avatar"

    def membership_badge(self, obj):
        colors = {
            "bronze": {"bg": "#f59e0b", "text": "#111827", "label": "Bronze"},
            "prata": {"bg": "#d1d5db", "text": "#111827", "label": "Prata"},
            "ouro": {"bg": "#facc15", "text": "#111827", "label": "Ouro"},
        }
        config = colors.get(obj.membership_type, {"bg": "#e5e7eb", "text": "#111827", "label": obj.membership_type})
        return format_html(
            '<span style="background:{}; color:{}; padding:4px 10px; border-radius:999px; font-weight:600; font-size:12px;">{}</span>',
            config["bg"],
            config["text"],
            config["label"],
        )
    membership_badge.short_description = "Plano"