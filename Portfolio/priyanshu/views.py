from django.shortcuts import render,HttpResponse
from priyanshu.models import Contact
def Contact_view(request):
    if request.method == "POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        contact_data=Contact(name=name,contact=contact,email=email)
        contact_data.save()
    return render(request,"Contact.html")
def About(request):
    return render(request,"About.html")
def Services(request):
    return render(request,"Services.html")
def Index(request):
    return render(request,"Index.html")
def Projects(request):
    return render(request,"Projects.html")

# Create your views here.
