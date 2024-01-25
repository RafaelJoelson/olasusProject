# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, cns, nome, login, senha=None, psf=None, area=None, **extra_fields):
        if not cns:
            raise ValueError('O CNS é obrigatório para criar um Agente de Saúde.')
        user = self.model(
            cns=cns,
            nome=nome,
            login=login,
            psf=psf,
            area=area,
            **extra_fields
        )
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, cns, nome, login, senha=None, psf=None, area=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(cns, nome, login, senha, psf, area, **extra_fields)

class AgentedeSaude(AbstractBaseUser):
    cns = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=255)
    login = models.CharField(max_length=255, unique=True)
    psf = models.CharField(max_length=10)
    area = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['cns', 'nome']

    def __str__(self):
        return self.nome
