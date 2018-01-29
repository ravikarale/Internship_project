from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# from django.core.context_processors import csrf
from django.template.context_processors import csrf
from pcm.models import Students
from myadmin.forms import pcmForm
from .models import addpcm
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib import auth


class AutoLogoutAdmin:
	def process_request(self,request):
		try:
			if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
				del request.session['uname']        			
				return render(request ,'admin_login.html')
        			
        		
    		except KeyError:
			pass

		request.session['last_touch'] = datetime.now()



def login(request):
	#c = {}
	#c.update(csrf(request))
	if request.session.get('uname'):    
        	return render(request, 'admin_home.html', {'some_flag': True})
        else:
		return render(request, 'admin_login.html', {'some_flag': False})
	# return render_to_response('admin_login.html',c)

def admin_logout(request):
	if request.session.get('uname'): 
		del request.session['uname']
        	return render(request ,'admin_login.html')
    	return render(request ,'admin_home.html')

	# return render_to_response('admin_login.html')
def getAdminLogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username=="ravi" and password=="karale":
            		request.session['uname']=username
			request.session['last_touch']=datetime.now()

        	if request.session.get('uname'):    
                	return render(request, 'admin_home.html', {'some_flag': True})
        	else:
            		return render(request, 'admin_login.html', {'some_flag': True})


		# 	return render_to_response('admin_home.html',{'some_flag': False})
		# else:
		# 	return render(request,'admin_login.html',{'some_flag':True})

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

def displayComapnyFinal(request):
    query_results = Students.objects.filter(placeType__startswith='Final')
    
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
            obj = addpcm(rollno=rollno,name=name,emailaddress=emailaddress,username=username,password=password)
            obj.save()

            
        else:
            #return render(request,'index.html')
            form=pcmForm()
        
    query_results = addpcm.objects.all()
    return render(request,'index.html',{'query_results':query_results})
    
