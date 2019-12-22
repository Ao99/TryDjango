from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_list_view(request):
    queryset = Product.objects.all()
    context={
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)
    
def product_detail_view(request, currId):
    # obj = Product.objects.get(id=currId)
    obj = get_object_or_404(Product, id=currId)
    # try:
    #     obj = Product.objects.get(id=currId)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        'object': obj
    }
    return render(request,'products/product_detail.html',context)
    
def product_edit_view(request, currId):
    # obj=Product.objects.get(id=1)
    obj=get_object_or_404(Product, id=currId)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'products/product_edit.html', context)
    
def product_delete_view(request, currId):
    obj=get_object_or_404(Product, id=currId)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context={
        'object':obj
    }
    return render(request,'products/product_delete.html',context)

def product_create_view(request):
    initial_data = {
        'title': 'red wine',
        'summary': 'some fake summary...'
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()
        
    context = {
        'form': form
    }
    return render(request,'products/product_create.html', context)
    
def product_create2_view(request):
    form = RawProductForm() # or RawProductForm(request.GET)
    if request.method == 'POST':
        form = RawProductForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        Product.objects.create(**form.cleaned_data)
        form = RawProductForm()
    else:
        print(form.errors)
    context = {
        'form': form
    }
    return render(request,'products/product_create2.html', context)
    
def product_search_view(request):
    # print(request.GET)
    # print(request.GET.get('q'))
    # print(request.POST)
    # print(request.POST.get('q'))
    context = {
        
    }
    return render(request,'products/product_search.html',context)