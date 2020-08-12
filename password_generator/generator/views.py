from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    content = {
        'password':'random generate password : blablabsadwqe022'
    }
    return render(request,'generator/home.html', content)