from django.db import models

# Create your models here.

class Categoria(models.Model):
    desc = models.CharField(max_length=200)


class Produto(models.Model):
    desc_produto = models.CharField(max_length=200)
    preco = models.DecimalField('Preço (R$)',max_digits=8, decimal_places=2)
    modelo_produto = models.CharField('Modelo', max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)



