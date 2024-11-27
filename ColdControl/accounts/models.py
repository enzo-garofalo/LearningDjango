#                                   Model
# É responsável por representar a estrutura e a lógica de dados da aplicação. 
# Ele define como os dados serão acessados, manipulados e armazenados, 
# assim como faz a interação com o banco de dados.
# ==========================================================================================================
# O Django utiliza o ORM (Object-Relational Mapping), 
# que permite que você utilize classes e objetos no Python para mapear 
# as tabelas do banco de dados, fazendo a criação, consulta, atualização e 
# exclusão de dados com mais segurança e facilidade.
# ==========================================================================================================
# Isso permite que você trabalhe com banco de dados relacionais sem ter a necessidade de lidar com SQL diretamente. 
# Além disso, você pode trabalhar com vários sistemas de 
# gerenciamento de banco de dados relacionais utilizando a mesma sintaxe e API.

from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True, verbose_name="User Id")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # Define o 'email' como o campo de login
    REQUIRED_FIELDS = ['username']  # O 'username' será necessário para a criação de um superusuário, por exemplo
    
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def showCreationDate(self):
        return self.created_at