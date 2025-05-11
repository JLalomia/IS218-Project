from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
    path('ExplorePlatforms/', views.explore_platforms, name='Explore'),
    path('explore/<int:pk>/reviews/', views.explore_reviews, name='explore_reviews'),
    path('admin-feedback-report/', views.feedback_report, name='feedback_report')
]

#path('', views.index, name='index'),
#path('about/', views.about, name='about'),
#path('contact/', views.contact, name='contact'),
#path('products/', views.products, name='products'),
#path('services/', views.services, name='services'),
#path('blog/', views.blog, name='blog'),
    
'''
    path('feedback-report/', views.feedback_report, name='feedback_report'),
    
    path('test', views.index),
    #path("homepage/", views.home, name='homepage'),
    path('', views.home, name='homepage'),
    path('KhanAcademy/', views.Khan, name='KhanAcademy'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),
    #path('ExplorePlatforms/', views.Explore, name="Explore"),
    path('ExplorePlatforms/', views.explore_platforms, name="Explore"),
    path('explore/<int:pk>/reviews/', views.explore_reviews, name='explore_reviews'),
    #path('e_p/<str:any_name>', views.base, name="base") # name paremeter: A unique name to refer to the route elsewhere (like in templates or redirects)
'''
