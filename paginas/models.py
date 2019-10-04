from django.db import models

class Produto(models.Model):
    codigo = models.CharField(max_length=30)
    nome = models.CharField(max_length=80)
    preco = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return self.codigo[:20]

class Orcamento(models.Model):
    codigo = models.IntegerField()
    data = models.DateField(auto_now=False, auto_now_add=False, null=True)
    status = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=5, null=True)
  
    def __str__(self):
        return self.status[:20]

class ItemOrcamento(models.Model):
    codigo_item = models.IntegerField()
    codigo_orcamento = models.IntegerField()
    codigo_produto = models.IntegerField()
    quantidade = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return self.codigo_item[:20]
