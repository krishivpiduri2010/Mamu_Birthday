from django.shortcuts import render

# Create your views here.
def home(request,joke_num):
    return render(request,'index.html',{'url':str(joke_num+1)})