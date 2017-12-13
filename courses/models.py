from django.db import models
from django.urls import reverse

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
