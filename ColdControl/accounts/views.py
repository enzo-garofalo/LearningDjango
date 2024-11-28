#                                               View
# ==========================================================================================================
# É responsável por processar as solicitações HTTP do usuário e retornar as respostas desse processamento. 
# As views são funções e classes que lidam com a lógica de negócios da aplicação, 
# sendo projetadas para serem reutilizáveis e utilizadas em diferentes aplicações de um mesmo projeto.
# ==========================================================================================================
# As views recebem as solicitações do usuário e consultam ou manipulam os dados nos modelos para retornar uma
#  resposta HTTP adequada à solicitação, como uma página HTML, um arquivo JSON, um arquivo de imagem, 
# dentre outros diversos formatos.
# ==========================================================================================================


from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse

from .models import User

# Quero que uma view login, vai receber email e senha
# Se corresponder redirecionar para página de home
# Senão retornar um alert dizendo email ou senha incorretos

def login(request):
    return render(request, "accounts/login.html")

def validateUser(request):
    if request.method == 'POST':
        email = request.POST.get('fEmail')
        password = request.POST.get('fPassword')
        print(email, password)

        

        if isUser(email, password):
            user = authenticate(request, email=email, password=password)

            # Essa função serve para atribuir request.user ao usuário autenticado
            # Você pode usar request.user em qualquer view, template ou middleware 
            # para personalizar a experiência, verificar permissões ou exibir informações específicas 
            # do usuário.
            auth_login(request, user)
            return redirect('camaraView:home')
        else:
            messages.error(request, 'Email ou senha incorretos')
            redirect('accounts:login')
    
    return redirect('accounts:login')

def isUser(email, password):
    if User.objects.filter(email=email, password=password):
        return True
    return False

# Quero ter uma view de signUp
def signUP(request):
    template = loader.get_template("accounts/signup.html")
    return render(request, "accounts/signup.html")

def createNewUser(request):
    if request.method == 'POST':
        name = request.POST.get('fName')
        # Ele faz a requisição pelo name das tags html!
        email = request.POST.get('fEmail')
        password = request.POST.get('fPassword')
    
        # Verifica se todos os parametros forma enviados
        if not all ([name, email, password]):
            messages.error(request, 'Please fill out all the fields!')
            return redirect('accounts:signUP')
        
        # Verifica se email já está no bd
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
            return redirect('accounts:signUP')

        # instancia objeto a classe user, com isso salva no bd
        newUser = User(name=name, email=email, password=password)
        newUser.save()

        messages.success(request, 'New account created, sign In to have access')
        return redirect('accounts:login')
   
    return redirect('accounts:signUP')