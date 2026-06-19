from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Categorias"


class Prato(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.preco < 0:
            raise ValidationError("O preço não pode ser negativo.")

    class Meta:
        verbose_name_plural = "Pratos"


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidade = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.numero}"

    class Meta:
        verbose_name_plural = "Mesas"


class Pedido(models.Model):
    ESTADOS = [
        ('pendente', 'Pendente'),
        ('em_preparacao', 'Em Preparação'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    pratos = models.ManyToManyField(Prato)
    data = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendente')

    def __str__(self):
        return f"Pedido #{self.id} - Mesa {self.mesa.numero}"

    class Meta:
        verbose_name_plural = "Pedidos"
