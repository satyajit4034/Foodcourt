from django.shortcuts import render

# Create your views here.
def chickenbiriyani(request):
    return render(request,'chickenbiriyani.html')

def rasgola(request):
    return render (request,'rasgola.html')