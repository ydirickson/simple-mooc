from django.db import models
from django.urls import reverse
from django.conf import settings

class Course(models.Model):

    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Atalho")
    short_description = models.CharField("Descrição Curta", max_length=100, blank=True)
    description = models.TextField("Descrição", blank=True)
    start_date = models.DateField("Data de Início", null=True, blank=True)
    image = models.ImageField(
        upload_to="courses/images",
        verbose_name="Imagem",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:detail", args=[self.slug])

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["name"]

class Enrollment(models.Model):

    STATUS_CHOICES = (
        (0, "Pendente"),
        (1, "Aprovado"),
        (2, "Cancelado"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name="Usuário",
        related_name="enrollments"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.DO_NOTHING,
        verbose_name="Curso",
        related_name="enrollments"
    )
    status = models.IntegerField(
        "Situação",
         choices=STATUS_CHOICES,
         default=0,
         blank=True
    )

    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def activate(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        unique_together = (
            ("user","course"),
        )