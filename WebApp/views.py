from unicodedata import name
from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import UserProfile
import pdfkit
from django.template import loader,Context
from django.template.loader import get_template
import io 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method== 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}! Your account has been successfully created.')
            return redirect('login')

    else:        
       form= UserCreationForm()
       return render(request, 'register.html',{'form':form})

def login(request):
    login(request)
    return redirect('user')

def user(request):
    if request.method=="POST":
       name=request.POST.get("name","")
       email=request.POST.get("email","")
       mobile=request.POST.get("mobile","")
       summary=request.POST.get("summary","")
       degree=request.POST.get("degree","")
       school=request.POST.get("school","")
       university=request.POST.get("university","")
       experience=request.POST.get("experience","")
       skills=request.POST.get("skills","")
    
       userprofile= UserProfile(name=name,email=email,mobile=mobile,summary=summary,degree=degree,school=school,university=university,experience=experience,skills=skills)
       userprofile.save()
    return render(request,'UserData.html')


def cv(request,id):
    profile=UserProfile.objects.get(id=id)
    template= loader.get_template('cv.html')
    html= template.render({'profile':profile})
    options= {
        'page-size': 'Letter',
        'encoding':"UTF-8",
    }

    config= pdfkit.configuration(wkhtmltopdf=r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdf= pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] = 'attachment;filename=cv.pdf'

    return response

def userList(request):
    profiles=UserProfile.objects.all()
    return render(request,'list.html',{'profiles': profiles})    

def delete(request,id):
    
    print(request.method)
    if request.method == 'POST':
        # item=UserProfile.objects.get(name=id)
        # item.delete()
        # print('Inside POST condition')
        profiles = UserProfile.objects.all()
        return render(request,'list.html',{'profiles':profiles})
    else:
        item=UserProfile.objects.get(name=id)
        item.delete()
        print('Inside POST condition')
        profiles = UserProfile.objects.all()
        return render(request,'list.html',{'profiles':profiles})   

@login_required
def profilepage(request):
    return render(request,'profile.html')    








