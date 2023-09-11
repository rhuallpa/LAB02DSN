from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import Persona


# Búsqueda

# Listado

def persona(request):
    personas = Persona.objects.all()
    return render(request, 'GestionPersona.html', {'personas': personas})

# Registro


def registrar_persona(request):
    id_persona = request.POST["id_persona"]
    dni = request.POST["dni"]
    apellidos = request.POST["apellidos"]
    nombres = request.POST["nombres"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    direccion = request.POST["direccion"]

    persona = Persona.objects.create(
        id_persona=id_persona,
        dni=dni,
        apellidos=apellidos,
        nombres=nombres,
        telefono=telefono,
        email= email,
        direccion= direccion
        
    )

    return redirect('/persona')

# Eliminar

def eliminar_persona(request, id_persona):
    persona = Persona.objects.get(id_persona=id_persona)
    persona.delete()
    return redirect('/persona')

# Edición

def edicion_persona(request, id_persona):
    persona = Persona.objects.get(id_persona=id_persona)
    return render(request, "EdicionPersona.html", {"persona": persona})

# Editar

def editar_persona(request, id_persona):
    if request.method == "POST":
        dni = request.POST["dni"]
        apellidos = request.POST["apellidos"]
        nombres = request.POST["nombres"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
 
        persona = Persona.objects.get(id_persona=id_persona)
        persona.dni = dni
        persona.apellidos = apellidos
        persona.nombres = nombres
        persona.telefono = telefono
        persona.email = email
        persona.direccion = direccion
        persona.save()

        return redirect('/persona')

    else:
        persona = Persona.objects.get(id_persona=id_persona)
        return render(request, 'EdicionPersona.html', {'persona': persona})











# vistas de login y demas, mas no de las tablas empleadas

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'Signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form})
   
def homes(request): 
    return render(request, 'Home.html')
   
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'Login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})
  
def profile(request): 
    return render(request, 'Profile.html')
   
def signout(request):
    logout(request)
    return redirect('/')
