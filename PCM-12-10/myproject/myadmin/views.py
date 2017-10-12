from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from pcm.models import Students
from myadmin.forms import pcmForm
from .models import addpcm
from passlib.hash import sha256_crypt

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('admin_login.html',c)

def backToLogin(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('admin_home.html',c)

def admin_logout(request):
	return render_to_response('admin_login.html')

def getAdminLogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username=="ravi" and password=="karale":
			return render_to_response('admin_home.html',{'some_flag': False})
		else:
			return render(request,'admin_login.html',{'some_flag':True})

def displayAdminFinal(request):
    query_results = Students.objects.filter(placeType__startswith='Final')
    
    context = {
    'adminStudents': query_results
    }
    return render_to_response('admin_home.html',context ) 

def displayAdminIntern(request):
    query_results = Students.objects.filter(placeType__startswith='Intern')
    
    context = {
    'adminStudents': query_results
    }
    return render_to_response('admin_home.html',context ) 


def callAddMember(request):
    c={}
    c.update(csrf(request))
    return render_to_response('create.html',c)

def addPcm(request):
    if request.method == 'POST':
        form = pcmForm(request.POST)
        if form.is_valid():
            rollno = request.POST['rollno']
            name = request.POST['name']
            emailaddress=request.POST['emailaddress']
            username = request.POST['username']
            password = request.POST['password']
            # password = sha256_crypt.encrypt( password )
            obj = addpcm(rollno=rollno,name=name,emailaddress=emailaddress,username=username,password=password)
            obj.save()

            
        else:
            #return render(request,'index.html')
            form=pcmForm()
        
    query_results = addpcm.objects.all()
    return render(request,'index.html',{'query_results':query_results})
    