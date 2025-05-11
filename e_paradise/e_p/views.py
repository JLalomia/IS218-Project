from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Product, Review
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.db.models import Avg


from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the e_paradise index.")


@staff_member_required # This decorator ensures that only staff members can access this view
def feedback_report(request):
    print("feedback_report view is active") # This will print in the console when the view is accessed
    try:
        reviews = Review.objects.all() # Fetch all reviews from the database
        print(f"Found {reviews.count()} reviews") # This will print the number of reviews found
    except Exception as e:
        print(f"❌ Error fetching reviews: {e}") # This will print any error on the terminal that occurs while fetching reviews
        return HttpResponse("❌ Error fetching reviews") #this will return an error message to the user if fetching reviews fails
    
    # If the reviews are fetched successfully, render the template with the reviews
    try:
        return render(request, 'e_p/feedback_report.html', {'reviews': reviews}) #i
    except Exception as e:
        print(f"❌ Error rendering template: {e}") # This will print any error on the terminal that occurs while rendering the template
        return HttpResponse(f"❌ Template error: {e}") #this will return an error message to the user if rendering the template fails


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
    
    
def ProductTemp(request):
    print(request.build_absolute_uri())
    return render(
        request, 'e_p/ProductTemp.html')
    
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
