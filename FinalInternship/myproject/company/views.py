from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# from django.core.context_processors import csrf
from django.template.context_processors import csrf
# from passlib.hash import sha256_crypt 
from django.conf import settings
from django.contrib.auth import logout
import csv,codecs,io
from django.core.files.storage import FileSystemStorage
from pcm.models import Students
from company.models import Company
from pcm.forms import StudentsForm


def company_home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('company_home.html',c)

def call_company_reg(request):
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

def company_registraion(request):
    if request.method == 'POST':
        CompanyName = request.POST['companyname']
        ContactPerson = request.POST['contactperson']
        Desig = request.POST['designation']
        Phone = request.POST['phone']
        Fax = request.POST['fax']
        Website = request.POST['website']
        Email = request.POST['email']
        BriefComProf = request.POST['bcprofile']
        FPosOff = request.POST['fposoffered']
        FNoOffVac = request.POST['fnumofvacancies']
        FJobLoc = request.POST['fjoblocation']
        FBenifits = request.POST['fcomp&benefits']
        FSelProc = request.POST.getlist('fradio')
        IPosOff = request.POST['iposoffered']
        INoOffVac = request.POST['inumofvacancies']
        IJobLoc = request.POST['ijoblocation']
        IBenifits = request.POST['icomp&benefits']
        ISelProc = request.POST.getlist('iradio')
        Facility = request.POST.getlist('fcheckbox')
        obj = Company(CompanyName=CompanyName,ContactPerson=ContactPerson,Desig=Desig,Phone=Phone,Fax=Fax
            ,Website=Website,Email=Email,BriefCompanyProfile=BriefComProf,FinalPosOff=FPosOff,FinalNoOfVac=FNoOffVac,
            FinalJobLoc=FJobLoc,FinalBenefits=FBenifits,FinalSelectionProc=FSelProc[0],InternPosOff=IPosOff,
            InternNoOfVac=INoOffVac,InternJobLoc=IJobLoc,InternBenefits=IBenifits,InternSelectionProc=ISelProc[0],
            FacilityReq=Facility[0])
        obj.save()

    return HttpResponse("Thank You So Much For The Felling The Form...")


        








