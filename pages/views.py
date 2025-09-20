from django.shortcuts import render
# Create your views here.
def base(request):
    return render(request, 'pages/base.html',)

def about(request):
    ctx = {
        'name':' Ralph Barry O. Daculo',
        'id': ' 2023-10475', 
    }
    return render(request, 'pages/about.html',ctx)

def home(request):
    return render(request, 'pages/home.html')