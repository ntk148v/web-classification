from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'web_app/index.html',{'test':'test'})

def result(request):
    content = request.POST['message']
    return render(request,'web_app/result.html',{'content':content})