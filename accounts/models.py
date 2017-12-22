from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    
    email = models.EmailField("E-Mail", unique=True)
    name = models.CharField("Nome", max_length=100)
    is_active = models.BooleanField("Ativo?", default=True, blank=True)
    is_staff = models.BooleanField("Equipe?", default=False, blank=True)
    date_joined = models.DateTimeField(
        "Data de Entrada", auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return str(self)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"


class PasswordReset(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário",
        related_name="resets"
    )
    key = models.CharField("Chave", max_length=100, unique=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    confirmed = models.BooleanField("Confirmado", default=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.created_at)

    class Meta:
        verbose_name = "nova senha"
        verbose_name_plural = "novas senhas"
        ordering = ["-created_at"]