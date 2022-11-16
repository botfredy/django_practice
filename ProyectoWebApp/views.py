from django.shortcuts import HttpResponse, render


def home(request):
    #return HttpResponse("Home")
    return render(request,"ProyectoWebApp/home.html") 
def servicio(request):
    #return HttpResponse("Servicio")
    return render(request,"ProyectoWebApp/servicio.html")

def tienda(request):
    #return HttpResponse("Tienda")
    return render(request,"ProyectoWebApp/tienda.html")

def blog(request):
    #return HttpResponse("Blog")
    return render(request,"ProyectoWebApp/blog.html")

def contacto(request):
    #return HttpResponse("Contacto")
    return render(request,"ProyectoWebApp/contacto.html")





