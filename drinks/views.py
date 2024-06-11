from django.shortcuts import render

# Create your views here.
def eno(request):
    return render(request,'eno.html')

def lassi(request):
    return render(request,'lassi.html')