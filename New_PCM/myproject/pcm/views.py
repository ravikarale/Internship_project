from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from passlib.hash import sha256_crypt 
from django.conf import settings
from django.contrib.auth import logout
import csv,codecs,io
from django.core.files.storage import FileSystemStorage
from pcm.models import pcm,Students
from pcm.forms import StudentsForm,pcmForm
from django.core.mail import send_mail, EmailMessage

# send_mail(
#     'Hii',
#     'email thro. django.',
#     'karaleravi1005@gmail.com',
#     ['swaminisangale@gmail.com'],
#     fail_silently=False,
# )

def pcm_login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('pcm_login.html',c)

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

            if pcm.objects.filter(username=u,password=p).exists():
                return render_to_response('pcm_home.html',{'some_flag': False})
        else:
            form = pcmForm()
        
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
    return render(request ,'pcm_login.html')

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
    if request.method == 'POST':
        xth = request.POST['xth']
        xiith = request.POST['xiith']
        graduation = request.POST['graduation']
        cgpa = request.POST['cgpa']
        select = request.POST['select']
        print xth
        # query_results = Students.objects.filter(xth__gte = float(xth))
        query_results = Students.objects.filter(xth__gte = float(xth) , xiith__gte = float(xiith) , graduation__gte = float(graduation) , cgpa__gte = float(cgpa),placeType__startswith=select)

        context={
        'pcm_query_results': query_results
        }
        print context

    return render_to_response('pcm_home.html',context ) 

def getSelected(request):
    if request.method == 'POST':
        # ch = []
        ch = request.POST.getlist('selected')
        print ch 
        for a in ch:
            # for b in a:
            #     print b
            print a
        # print ch
    
    return HttpResponse("hi")

def sendTo(request):
    if request.method == 'POST':

        ch = request.POST.getlist('selected')
        print ch 
        
        # subject = "hii..."
        # message = "this email send thro. django."
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [from_email, 'pranalilokhande271@gmail.com']

        # email = EmailMessage(subject,message,from_email,to_email)
        # email.attach_file('/home/ravi/ravi/Download/Learn HTML and CSS with w3schools.pdf')
        # email.send()

        # send_mail(subject=subject,from_email=from_email,recipient_list=to_email, message=message,fail_silently=True)

    return HttpResponse("send")
