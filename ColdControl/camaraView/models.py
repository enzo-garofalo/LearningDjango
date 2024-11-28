from django.db import models

class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name="Nome do Produto",
        help_text="Nome completo do produto."
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Categoria",
        help_text="Categoria do produto (ex.: bombom, copinho, pote)."
    )
    qtty = models.PositiveIntegerField(
        verbose_name="Quantidade",
        help_text="Quantidade atual do produto em estoque."
    )

    def __str__(self):
        return f"{self.product_name} ({self.category}) - {self.qtty} unidades"

    # Adicionada para personalizar o nome e a ordem padrão dos registros.
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['product_name']
