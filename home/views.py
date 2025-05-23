from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "home/index.html")

def success_page(request):
    print("this is success page")
    return HttpResponse("<h1> this is success page  </h1>")












