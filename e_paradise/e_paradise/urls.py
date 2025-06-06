"""
URL configuration for e_paradise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('e_paradise/', include('e_p.urls')) #http://127.0.0.1:8000/e_paradise/test
    path('', include('e_p.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('e_p/', include('e_p.urls')), # Uncomment this line if you want to include the e_p app URLs

"""
Explanation of code so far:
we now registered our first view and the URLconfig for it.
And the URLconfig is actually split across two URLs py files.
One for the app, the e_p app,and one for the entire project (e-paradise folder).

P.s, the one for the entire project basically just is able to route requests that start with different paths.

"""