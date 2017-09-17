from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from pcm.models import Document
from pcm.forms import DocumentForm




# def pcm_login(request):
# 	c = {}
# 	c.update(csrf(request))
# 	return render_to_response('pcm_login.html',c)

def pcm_home(request):
		c = {}
		c.update(csrf(request))
		return render_to_response('pcm_home.html',c)

# def add(request):
#     if request.method == 'POST':
#     	username = request.POST['username']
#     	password = request.POST['password']
#     	pcm = pcm_auth(username=username,password=password)    	
#         pcm.save()
# 	return redirect('pcm_home.html')


def home(request):
    documents = Document.objects.all()
    return render(request, 'home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        with open('filename') as f:
            reader = csv.reader(f, delimiter=',')
            header = next(reader)
            student.objects.bulk_create([student(rollno=row[0], fName=row[1],lName=row[2]) for row in reader])
       #     console.log(filename)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)  
        # console.log(filename)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


    # with open('some/path/to/file.csv') as f:
    # reader = csv.reader(f, delimiter=',')
    # header = next(reader)
    # Foo.objects.bulk_create([Foo(first_name=row[0], last_name=row[1]) for row in reader])


    
    
    
    # with open(path) as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         _, created = Teacher.objects.get_or_create(
    #             first_name=row[0],
    #             last_name=row[1],
    #             middle_name=row[2],
    #             )
