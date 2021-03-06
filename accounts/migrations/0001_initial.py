# Generated by Django 2.0 on 2017-12-22 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-Mail')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Equipe?')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
            },
        ),
    ]
