# Generated by Django 5.0.3 on 2024-03-07 15:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Licao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('capa', models.ImageField(blank=True, upload_to='licoes/%Y/%m/')),
            ],
            options={
                'verbose_name': 'Licao',
                'verbose_name_plural': 'Licoes',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='usuarios/%Y/%m/')),
                ('licao_atual', models.IntegerField(default=1)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabecalho', models.TextField(blank=True)),
                ('texto', models.TextField(blank=True)),
                ('imagem', models.ImageField(blank=True, upload_to='perguntas/%Y/%m/')),
                ('tipo', models.CharField(choices=[('TX', 'Texto'), ('IM', 'Imagem')], default='TX', max_length=2)),
                ('licao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perguntas', to='duolinguas.licao')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True)),
                ('licao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='duolinguas.licao')),
            ],
        ),
    ]
