from django.shortcuts import render
from .models import team

def home(request):
    teams=team.objects.all()
    context={
    'teams': teams,
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request,'pages/about.html')

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')
