from django.urls import path
from . import views

urlpatterns = [
    path("test", views.index),
    path("e_p/<str:any_name>", views.base, name="base"), # name paremeter: A unique name to refer to the route elsewhere (like in templates or redirects)
    path("homepage", views.home)
    
    ]

#path('', views.index, name='index'),
#path('about/', views.about, name='about'),
#path('contact/', views.contact, name='contact'),
#path('products/', views.products, name='products'),
#path('services/', views.services, name='services'),
#path('blog/', views.blog, name='blog'),