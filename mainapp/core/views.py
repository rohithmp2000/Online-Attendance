from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def selectrole(request):
    if request.method =='GET':
        return render(request, 'selectrole.html')