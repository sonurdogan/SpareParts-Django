from django.shortcuts import render
from .models import Product
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request,"home.html", {'products': products})

def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})
def search(request):
	# Determine if they filled out the form
	if request.method == "POST":
		searched = request.POST['searched']
		# Query The Products DB Model
		searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
		# Test for null
		if not searched:
			messages.success(request, "That Product Does Not Exist...Please try Again.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})

def offer(request):
    products = Product.objects.filter(is_special_offer=True)
    return render(request,"offer.html", {'products': products})