from .base_de_dados import produtos
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ColdControl.settings')
django.setup()

from camaraView.models import Product

def create_product(name, category, qtty):
    newProduct = Product(product_name=name, category=category, qtty=qtty)
    newProduct.save()



def run():
    for tipo, valores in produtos.items():
        for nome in valores:
            print(f"Criando produto: {nome} na categoria {tipo}")
            create_product(name=nome, category=tipo, qtty=0) 