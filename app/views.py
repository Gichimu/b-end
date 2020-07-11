from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def properties(request):
    return render(request, 'property.html')