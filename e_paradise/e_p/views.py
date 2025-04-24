from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the e_paradise index.")


#function name "base" to match the html file under the subfolder e_p/templates/e_p/base.html
#the parameter "any_name" is a placeholder for the name we will pass in the URL and connects to the second path under urls.py in the e_p folder
def base(request, any_name): #any_name is the function parameter that catches what came from the URL
    print(request.build_absolute_uri()) #prints the full URL (like http://localhost:8000/hello/Emily) in the console
    return render(
            request, 
            'e_p/base.html',
            {   
                'name2': any_name, # sending '[insert name]]' to the hello_there.html template as 'name2'
                'date': datetime.now()
            }
            )

def home(request):
    print(request.build_absolute_uri())
    return render(
        request,
        'e_p/homepage.html',
    )