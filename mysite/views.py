from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from reportlab.pdfgen import canvas
from django.core.files import File
from django.conf import settings
from .forms import UploadFileForm
from django.middleware import csrf
import os


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    with open('/home/bear/Documents/code/bearicc.com/static/doc/resume.pdf', 'rb') as f:
        pdf = File(f)
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename="resume.pdf"'
        # p = canvas.Canvas(response)
        # p.drawString(100, 100, "Hello world.")
        # p.showPage()
        # p.save()
        return response
    pdf.closed
    f.closed


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            if (title == ""):
                title = request.FILES['file'].name
            handle_uploaded_file(title, request.FILES['file'])
            return HttpResponse("<h1>File :"+title+" uploaded!</h1>")
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))


def handle_uploaded_file(title, f):
    with open('/home/bear/Documents/code/bearicc.com/staticfiles/upload/'+title, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
