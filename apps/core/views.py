
from django.shortcuts import render


def home(request):
    return render(request, 'core/frontpage.html')


def blog(request):
    return render(request,'core/blog.html')

def about(request):
    return render(request,'core/about.html')        



def contact(request):
    
    return render(request,'core/contact.html')    

