from django.shortcuts import render,redirect
from store.models import Product	
from store.forms import ContactoForms , CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages




def Home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)


def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            ##Autentificar al registrar
            user=authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            ##redirigir al home
            return redirect(to='home')
        data["form"]=formulario
    return render(request,'registration/registro.html',data)

# def contact(request):
#     data = {
#         'form': ContactoForms()
#         # se instacia la clase forms del formulario
#     }
#     if request.method== 'POST':
#         formulario=ContactoForms(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             data["Mensaje"] = "    Su consulta fue enviada."
#         else:
#             data["form"]= formulario
#     return render(request,'store/contact.html',data)