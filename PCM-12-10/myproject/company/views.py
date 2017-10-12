from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
# from passlib.hash import sha256_crypt 
from django.conf import settings
from django.contrib.auth import logout
import csv,codecs,io
from django.core.files.storage import FileSystemStorage
from pcm.models import Students
from pcm.forms import StudentsForm


def company_home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('company_home.html',c)

def company_reg(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('company_reg.html',c)

def desplayCompanyFinal(request):
    # query_results = Students.objects.all() # display all records
    query_results = Students.objects.filter(placeType__startswith='Final')
    
    context = {
    'CompFinalStudents': query_results
    }

    return render(request,'company_home.html', context)

def desplayCompanyIntern(request):
    # query_results = Students.objects.all() # display all records
    query_results = Students.objects.filter(placeType__startswith='Intern')
    
    context = {
    'CompInternStudents': query_results
    }

    return render(request,'company_home.html', context)

def comp_criteria(request):
    if request.method == 'POST':

        xth = request.POST['xth']
        xiith = request.POST['xiith']
        graduation = request.POST['graduation']
        cgpa = request.POST['cgpa']
        Select = request.POST['select']
        print Select
        # query_results = Students.objects.filter(xth__gte = float(xth))
        query_results = Students.objects.filter(xth__gte = float(xth) , xiith__gte = float(xiith) , graduation__gte = float(graduation) , cgpa__gte = float(cgpa),placeType__startswith=Select)

        context={
        'query_results': query_results
        }
        print context

    return render_to_response('company_home.html',context ) 



