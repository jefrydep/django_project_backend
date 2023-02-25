# imortamor el modulo path para definir las rutas
from django.urls import path
from . import views


urlpatterns =[
     path('',views.hello),
    path('about/',views.about),

]