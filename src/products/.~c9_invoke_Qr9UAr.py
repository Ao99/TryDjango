from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        
    context = {
        'form': form
    }
    return render(request,'products/product_create.html', context)
    
def product_create2_view(request):
    form = RawProductForm(request)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,'products/product_create2.html', context)
    
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context={
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'summary': obj.summary,
    #     'featured': obj.featured,
    # }
    context = {
        'object': obj
    }
    return render(request,'products/product_detail.html',context)
    
def product_search_view(request):
    # print(request.GET)
    # print(request.GET.get('q'))
    # print(request.POST)
    # print(request.POST.get('q'))
    context = {
        
    }
    return render(request,'products/product_search.html',context)