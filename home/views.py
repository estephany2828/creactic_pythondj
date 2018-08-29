from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def quienes_somos_view(request):
  nombre = 'Juana la loca'
  #return render(request,'quienes_somos.html',{'n': nombre})
  return render(request, 'quienes_somos.html',locals())

def contactenos_view(request):
    email=""
    subject=""
    text=""
    if request.method=='POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            email     =formulario.cleaned_data['correo']
            subject   =formulario.cleaned_data['asunto']
            text      =formulario.cleaned_data['texto']
            info_enviado = True
            return render (request, 'contactenos.html', locals())
        else:
            msg = 'la informacion es correcta'
    else:
        formulario = contacto_form()

    return render(request,'contactenos.html',locals())

def nuestros_servicios_view(request):
  return render(request,'nuestros_servicios.html')

def inicio_view(request):
  return render(request,'inicio.html')

def lista_producto_view (request):
    lista = Producto.objects.filter()
    return render(request, 'lista_producto.html', locals())

def agregar_producto_view(request): 
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == 'POST':
            formulario = agregar_producto_form(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('/lista_producto/')
            else:
                msj="hay datos no validos"
        else:
            formulario = agregar_producto_form()
        return render(request, 'agregar_producto.html', locals())
    else:
        return redirect('/lista_producto/')

def ver_producto_view(request, id_producto):
    try:
        obj= producto.objects.get(id = id_prod)
    except:
        print("Error en la consulta el producto no existe")
        msj = "Error en la consulta el producto no exite"    
    return render(request, 'ver_producto.html', locals())  

    #variable obj almacena el producto
    #get es obligatrio colocarle una condicion
    #obtengamos un id de producto cuando id sea igual a1 si lo encuentra 

def editar_producto_view(request,  id_prod):
    obj= producto.objects.get(id = id_prod)
     #pasar la instancia de ese objeto
    if request.method == 'POST':
        formulario=agregar_producto_form(request.POST, request.FILES, instance=obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('/lista_producto/')
            #formulario.save(commit = False)
    formulario=agregar_producto_form(instance=obj)         
    return render(request, 'agregar_producto.html', locals())    

def eliminar_producto_view(request,  id_prod):
    obj= producto.objects.get(id=id_prod)
     #pasar la instancia de ese objeto
    obj.delete()
    return redirect('lista_producto')

    #para que no me los elimine todos

def desactivar_producto_view(request,  id_prod):
    obj= producto.objects.get(id=id_prod)
     #pasar la instancia de ese objeto
    obj.delete()
    return redirect('lista_producto')

    #para que no me los elimine todos 
    #cuales son los elementos importantes que traen request   

def login_view(request):
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            user = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username= user, password= cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/lista_producto/')
            else:
                msj = 'no se pudo iniciar sesion'   
    formulario=login_form()
    return render(request, 'login.html', locals())

def logout_view(request):
    logout(request)
    return redirect('/login/')    



def register_view(request):
	formulario=register_form()

	if request.method == 'POST':
		formulario=register_form(request.POST)
		if formulario.is_valid():

			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u= User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return redirect('/login/')
		else:
			msj= 'no se puedo crear el usuario'

	return render(request, 'register.html', locals())

def thanks_for_register_view(request):
	return render (request, 'register.html', locals())    

   

def servicio_web_view(request):
    data= serializers.serialize('json', Productos.objects.all())
    return httpResponse(data,content_type='aplication/json')