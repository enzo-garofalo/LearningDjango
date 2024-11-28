# Generated by Django 5.1.3 on 2024-11-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='Nome completo do produto.', max_length=100, verbose_name='Nome do Produto')),
                ('category', models.CharField(help_text='Categoria do produto (ex.: bombom, copinho, pote).', max_length=100, verbose_name='Categoria')),
                ('qtty', models.PositiveIntegerField(help_text='Quantidade atual do produto em estoque.', verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['product_name'],
            },
        ),
    ]