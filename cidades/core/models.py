from django.db import models

class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=20)


class Cidade(models.Model):
    nome = models.CharField(max_length=35)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __repr__(self):
        return str(f'{str(self.nome)} - {str(self.estado.sigla)}')

    def __str__(self):
        return f'{str(self.nome)} - {str(self.estado.sigla)}'
