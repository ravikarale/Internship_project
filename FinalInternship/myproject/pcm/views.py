from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
# from passlib.hash import sha256_crypt 
from django.conf import settings
from django.contrib.auth import logout
import csv,codecs,io
from django.core.files.storage import FileSystemStorage
from pcm.models import pcm,Students
from company.models import Company
from myadmin.models import addpcm
from pcm.forms import StudentsForm,pcmForm
from django.core.mail import send_mail, EmailMessage
from datetime import datetime, timedelta
from django.contrib import auth


class AutoLogoutPCM:
	def process_request(self,request):
		try:
			if datetime.now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
				del request.session['uname']        			
				return render(request ,'pcm_login.html')
        			
        		
    		except KeyError:
			pass

		request.session['last_touch'] = datetime.now()


# @csrf_protect
def pcm_login(request):
	# c = {}
	# c.update(csrf(request))
    	if request.session.get('uname'):
        	return render(request, 'pcm_home.html', {'some_flag': True})
   	else:
		return render(request, 'pcm_login.html', {'some_flag': False})

	# return render_to_response('pcm_login.html',c)

def pcm_home(request):
		c = {}
		c.update(csrf(request))
		return render_to_response('pcm_home.html',c)


  
def getLogin(request):
    if (request.method == 'POST'):
        form = pcmForm(request.POST)
        if form.is_valid():

            u = request.POST['username']
            p= request.POST['password']

            if addpcm.objects.filter(username=u,password=p).exists():
		request.session['last_touch']=datetime.now()
                request.session['uname']=u
                # return render_to_response('pcm_home.html',{'some_flag': False})
        # else:
            # form = pcmForm()
            if request.session.get('uname'):    
                return render(request, 'pcm_home.html', {'some_flag': True})
    return render(request, 'pcm_login.html', {'some_flag': True})

# def getLogin(request):
#     if (request.method == 'POST'):
#         username = request.POST['username']
#         password = request.POST['password']

#         pass_valid = sha256_crypt.verify(password , )
#         user_valid = sha256_crypt.verify(password , )

#         if (pcm.objects.filter(username=username).exists()) and :
#             return render_to_response('pcm_home.html',{'some_flag': False})
        
#         return render(request, 'pcm_login.html', {'some_flag': True})

  
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('upload.html',c)

def logout(request):
    if request.session.get('uname'): 
        del request.session['uname']
        return render(request ,'pcm_login.html')
    
    return render(request ,'pcm_home.html')
    # if request.session.get('uname'): 
    #     return render(request ,'pcm_login.html')
    # return render(request ,'pcm_home.html')

def upload(request):
    if request.method == 'POST' and request.FILES:
        csvfile = request.FILES['csv_file']
        dataReader = csv.reader(csvfile,delimiter=',')
        for row in dataReader:
            # print row
            rollNo = row[0]
            firstName = row[1]
            lastName = row[2]
            email = row[3]
            course = row[4]
            xth = row[5]
            xiith = row[6]
            graduation = row[7]
            cgpa = row[8]
            status = row[9]
            placeType = row[10]
            
            obj = Students(rollNo=rollNo,firstName=firstName,lastName=lastName,emailId=email,course=course,xth=xth,xiith=xiith,graduation=graduation,cgpa=cgpa,status=status,placeType=placeType)
            obj.save()


    return render(request,'upload.html', {'some_flag': True })

def desplayFinal(request):
    # query_results = Students.objects.all() # display all records
    query_results = Students.objects.filter(placeType__startswith='Final')
    
    context = {
    'PcmFinalStudents': query_results
    }

    return render(request,'pcm_home.html', context)

def desplayIntern(request):
    # query_results = Students.objects.all() # display all records
    query_results = Students.objects.filter(placeType__startswith='Intern')

    context = {
    'PcmInternStudents': query_results
    }

    return render(request,'pcm_home.html', context)    

def pcm_criteria(request):
    if request.method == 'POST' :
        xth = request.POST['xth']
        xiith = request.POST['xiith']
        graduation = request.POST['graduation']
        cgpa = request.POST['cgpa']
        select = request.POST['select']
        print select
        # query_results = Students.objects.filter(xth__gte = float(xth))
        query_results = Students.objects.filter(xth__gte = float(xth) , xiith__gte = float(xiith) , graduation__gte = float(graduation) , cgpa__gte = float(cgpa),placeType__startswith=select)

        context={
        'pcm_query_results': query_results
        }
        print context

    return render_to_response('pcm_home.html',context ) 


def send(request):
    if request.method == 'GET':
        ch = request.GET.getlist('selected')
        # ch = [int(s) for s in ch if s.isdigit()]
        print "send",ch
        c = {}
        c.update(csrf(request))
        # query_results = Students.objects.all() # display all records
        results = Company.objects.all()
        context={
        'c':c,
        'ch': ch,
        'results':results    
        }
    return render(request,'send.html',context)

def emailSend(request):  
    if request.method == 'POST':
        to = request.POST['drop1']
        ch = request.POST['selected_id']
        print ch 
        # ch = [int(s) for s in ch if s.isdigit()]
        ch = ch[1:-1]+","
        print ch
        ch = ch.split(',')
        ch = [int(s) for s in ch if s.isdigit()]
        for i in ch:
            print i
        subject = request.POST['subject']      
        message = request.POST['msg']
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,str(to)]
        
        email = EmailMessage(subject,message,from_email,to_email)
        for i in ch:
            results = Students.objects.filter(id=i)
            for j in results:
                fname=str(j.rollNo)+"_"+str(j.firstName)+"_"+str(j.lastName)+".pdf"
                # print fname
                email.attach_file('/home/ravi/PCM/Pdfs/'+fname)
        
        email.send()

    return HttpResponse("Selected Students Resumes Are Send To The HR...")



# def sendTo(request):
#     if request.method == 'GET':   
#         subject = "Students resume...!"         
#         message = "this email send thro. django."         
#         from_email =settings.EMAIL_HOST_USER
#         to_email = [from_email,from_email,'vidyatmagic@gmail.com']
#         email = EmailMessage(subject,message,from_email,to_email)
#         print email
#         ch = request.GET.getlist('selected')
#         for i in ch:
#             results = Students.objects.filter(id=i)
#             for j in results:
#                 fname=str(j.rollNo)+"_"+str(j.firstName)+"_"+str(j.lastName)+".pdf"
#                 email.attach_file('/home/ravi/PCM/Pdfs/'+fname)
       
#         email.send()

#     return HttpResponse("Selected Students Resumes Are Send To The HR...")

         
