from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples = [
        {"name": "John", "age": 25},
        {"name": "Jane", "age": 15},  
        {"name": "Bob", "age": 35},
    ]
    text = """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt iure tempora nesciunt atque, nam modi in provident repellendus vel beatae!"""
    
    return render(request, "home/index.html", context = {"peoples": peoples, "text": text , 'page': 'home'} )


def success_page(request):
    print("this is success page")
    return HttpResponse("<h1> this is success page  </h1>")

def about(request):
    context = {'page':'about  '}
    return  render(request, "home/about.html",context)
def contact(request):
    context = {'page':'contact  '}
    return  render(request, "home/contact.html",context)










