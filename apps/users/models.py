from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


GENERO_CHOICES = (
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("O", "Outro"),
    ("N", "Prefiro não informar"),
)

MEMBERSHIP_CHOICES = (
    ("bronze", "Bronze"),
    ("prata", "Prata"),
    ("ouro", "Ouro"),
)

IDIOMA_CHOICES = (
    ("pt-br", "Português (Brasil)"),
    ("en", "English"),
    ("es", "Español"),
)


telefone_validator = RegexValidator(
    regex=r"^\+?[\d\s\-\(\)]{10,20}$",
    message="Informe um telefone válido.",
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O campo email é obrigatório.")

        email = self.normalize_email(email)

        username = extra_fields.get("username")
        if not username:
            base_username = email.split("@")[0].strip().lower().replace(" ", "")
            username = f"{base_username}_{uuid4().hex[:6]}"
            extra_fields["username"] = username

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("terms_accepted", True)
        extra_fields.setdefault("data_terms_accepted", timezone.now())

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário precisa ter is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário precisa ter is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField("E-mail", unique=True)

    telefone = models.CharField(
        "Telefone",
        max_length=20,
        blank=True,
        null=True,
        validators=[telefone_validator],
    )
    telefone_whatsapp = models.BooleanField("É WhatsApp", default=False)
    data_nascimento = models.DateField("Data de nascimento", blank=True, null=True)
    genero = models.CharField(
        "Gênero",
        max_length=20,
        choices=GENERO_CHOICES,
        blank=True,
        null=True,
    )
    cpf_cnpj = models.CharField(
        "CPF/CNPJ",
        max_length=18,
        blank=True,
        null=True,
        unique=True,
    )
    avatar = models.ImageField(
        "Avatar",
        upload_to="avatars/",
        blank=True,
        null=True,
    )
    bio = models.TextField("Biografia", blank=True, null=True)
    website = models.URLField("Website", blank=True, null=True)
    rede_social = models.JSONField("Redes sociais", default=dict, blank=True)
    receber_newsletter = models.BooleanField("Receber newsletter", default=False)
    terms_accepted = models.BooleanField("Aceitou os termos", default=False)
    data_terms_accepted = models.DateTimeField(
        "Data de aceite dos termos",
        blank=True,
        null=True,
    )
    membership_type = models.CharField(
        "Tipo de membro",
        max_length=20,
        choices=MEMBERSHIP_CHOICES,
        default="bronze",
    )
    latitude = models.DecimalField(
    "Latitude",
    max_digits=9,
    decimal_places=6,
    blank=True,
    null=True,
    )       

    longitude = models.DecimalField(
        "Longitude",
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )
        
    cidade = models.CharField("Cidade", max_length=100, blank=True, null=True)
    estado = models.CharField("Estado", max_length=50, blank=True, null=True)
    pais = models.CharField("País", max_length=50, blank=True, null=True)
    idioma = models.CharField(
        "Idioma",
        max_length=10,
        choices=IDIOMA_CHOICES,
        default="pt-br",
    )
    timezone = models.CharField(
        "Fuso horário",
        max_length=50,
        default="America/Sao_Paulo",
    )
    metadata = models.JSONField("Metadados", default=dict, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.get_full_name() or self.email

    @property
    def nome_completo(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()
    @property
    def telefone_formatado(self):
        if not self.telefone:
            return ""

        numero = "".join(filter(str.isdigit, self.telefone))

        if len(numero) == 11:
            return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
        if len(numero) == 10:
            return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
        return self.telefone

    def save(self, *args, **kwargs):
        if not self.username:
            base_email = self.email.split("@")[0].strip().lower().replace(" ", "")
            self.username = f"{base_email}_{uuid4().hex[:6]}"

        if self.terms_accepted and not self.data_terms_accepted:
            self.data_terms_accepted = timezone.now()

        super().save(*args, **kwargs)