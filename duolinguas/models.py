from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(blank=True, upload_to='usuarios/%Y/%m/')
    licao_atual = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.usuario.username}'
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'


class Licao(models.Model):
    nome = models.CharField(max_length=50)
    capa = models.ImageField(blank=True, upload_to='licoes/%Y/%m/')

    class Meta:
        verbose_name = 'Licao'
        verbose_name_plural = 'Licoes'


class Pergunta(models.Model):
    class Tipo(models.TextChoices):
        TEXTO = 'TX', 'Texto'
        IMAGEM = 'IM', 'Imagem'


    cabecalho = models.TextField(blank=True)
    texto = models.TextField(blank=True)
    imagem = models.ImageField(blank=True, upload_to='perguntas/%Y/%m/')
    tipo = models.CharField(max_length=2, 
        choices=Tipo.choices, default=Tipo.TEXTO)
    licao = models.ForeignKey(Licao,
        on_delete=models.CASCADE, related_name='perguntas')


class Resposta(models.Model):
    texto = models.TextField(blank=True)
    licao = models.ForeignKey(Licao,
        on_delete=models.CASCADE, related_name='respostas')

