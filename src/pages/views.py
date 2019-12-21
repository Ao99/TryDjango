from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home_view(request, *args,**kwargs):
    # TODO: write code...
    print('request:', request)
    print('request user:', request.user)
    print(args, kwargs)
    return render(request,"home.html",{})
    
def contact_view(request, *args,**kwargs):
    return render(request,"contact.html",{})    
    
def about_view(request, *args,**kwargs):
    my_context = {
        'author': 'the author is Ao Dong',
        'context_introduction': 'The website is about Django learning',
        'context_number': 123456,
        'context_list': [123,234,345,456,567,'abc','zxc'],
        'html': '<h1>Hello World!</h1>',
        'datetime': datetime.datetime.now(),
    }
    return render(request,"about.html",my_context)
    
def products_view(request, *args,**kwargs):
    return render(request,"products.html",{})