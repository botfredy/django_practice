#from django.contrib import admin
from django.urls import path

from ProyectoWebApp import views

#import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home,name="Home"),
    path('servicio', views.servicio,name="Servicio"),
    path('tienda', views.tienda,name="Tienda"),
    path('blog', views.blog,name="Blog"),
    path('contacto',views.contacto,name="Contacto"),
]