from django.shortcuts import render,HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        "variable1" : "this is sent",
        "variable2" : "My name is Utsav"
    }
    return render(request,'home.html')
    #return HttpResponse("This is our Home page..")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about page ...")

def blog(request):
    return render(request,'blog.html')
    #return HttpResponse("This is  services page ...")

def contactus(request):
    messages.success(request,'welcome to contact..')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['contact']
        print(name,email,phone,content)
        contact = contact(name = name,email=email,phone=phone,content=content)
        contact.save()
    return render(request,'contactus.html')