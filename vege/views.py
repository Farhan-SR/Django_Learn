from django.shortcuts import render ,redirect
from .models import *
# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST 
        receipe_name = data["receipe_name"]
        receipe_descriptions = data["receipe_descriptions"]
        receipe_image = request.FILES.get("receipe_image")
        print(data)
        print(receipe_image)
        
        
        Receie.objects.create(
            receipe_name = receipe_name,
            receipe_descriptions = receipe_descriptions,
            receipe_image = receipe_image
        )
        
        return redirect("/receipes/")
    
    
    
    return render(request, "receipes.html") 