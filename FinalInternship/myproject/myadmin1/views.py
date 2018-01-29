from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from pcm.models import Students


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('admin_login.html',c)

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
    print "ok"
    return render_to_response('admin_home.html',context ) 

def displayAdminIntern(request):
    query_results = Students.objects.filter(placeType__startswith='Intern')
    
    context = {
    'adminStudents': query_results
    }
    print "ok"
    return render_to_response('admin_home.html',context ) 