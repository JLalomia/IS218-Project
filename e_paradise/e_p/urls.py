from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('test', views.index),
    path('e_p/<str:any_name>', views.base, name="base"), # name paremeter: A unique name to refer to the route elsewhere (like in templates or redirects)
    #path("homepage/", views.home, name='homepage'),
    path('', views.home, name='homepage'),
    path('TempProductPage/', views.ProductTemp, name='TempProductPage'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
    #path('ExplorePlatforms/', views.Explore, name="Explore"),
    path('ExplorePlatforms/', views.explore_platforms, name="Explore"),
    
    ]

#path('', views.index, name='index'),
#path('about/', views.about, name='about'),
#path('contact/', views.contact, name='contact'),
#path('products/', views.products, name='products'),
#path('services/', views.services, name='services'),
#path('blog/', views.blog, name='blog'),