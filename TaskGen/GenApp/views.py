from django.shortcuts import render
from  django.http import  HttpResponse
from django.core.files.storage import FileSystemStorage  # Required for file handling
from .form import UploadMoM
# Create your views here.


def main(request):
    
    return render(request,'main.html')

def table(request):

    return render(request,'table.html')

def edit_table(request):

    return HttpResponse('you can edit the table')


def upload(request):
    if request.method == 'POST':
        form = UploadMoM(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'table.html')
    else:
        form = UploadMoM()
        context = {
            'form':form,
        }
    return render(request, 'upload.html', context)
