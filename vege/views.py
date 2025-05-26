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
    
    queryset = Receie.objects.all()
    context = {"receipes": queryset}
    
    return render(request, "receipes.html",context) 

def delete_receipe( request,id ):
    queryset = Receie.objects.get(id = id)
    queryset.delete()
    return redirect("/receipes/")

def update_receipe(request, id):
    queryset = Receie.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipes_image = request.FILES.get("receipe_image")
        receipes_name = data.get("receipe_name")  # ✅ FIXED
        receipes_descriptions = data.get("receipe_descriptions")

        if receipes_image:
            queryset.receipe_image = receipes_image  # Only update image if uploaded

        queryset.receipe_name = receipes_name
        queryset.receipe_descriptions = receipes_descriptions
        queryset.save()

        return redirect("/receipes/")

    context = {"receipe": queryset}
    return render(request, "update_receipe.html", context)


