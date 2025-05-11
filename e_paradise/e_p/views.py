from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Product, Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.db.models import Avg


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
    top_products = Product.objects.annotate(avg_rating=Avg('reviews__rating')) \
                                  .order_by('-avg_rating')[:3]
    return render(
        request,
        'e_p/homepage.html',{'top_products': top_products}
    )

def Khan(request):
    print(request.build_absolute_uri())
    return render(
        request, 'e_p/KhanAcademy.html')

def Login(request):
    print(request.build_absolute_uri())
    return render(request, 'e_p/Login.html')

def Signup(request):
    print(request.build_absolute_uri())
    return render(request, 'e_p/Signup.html')

def Explore(request):
    print(request.build_absolute_uri())
    return render(request, 'e_p/ExplorePlatforms.html')

def explore_platforms(request):
    products = Product.objects.all()
    form = ReviewForm()

    return render(request, 'e_p/ExplorePlatforms.html', {'products': products, 'form':form,})

def explore_reviews(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return render(request, '404.html', status=404)
    
    form = ReviewForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user    = form.cleaned_data['user']
        rating  = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']

        Review.objects.create(
            product=product,
            user=user,
            rating=rating,
            comment=comment
        )
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'e_p/product_review.html', {
        'product': product,
        'form': form,
    })
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)
    return render(request, 'e_p/product_detail.html', {
        'product': product,
        'reviews': reviews
    })