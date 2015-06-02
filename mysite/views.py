from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.core.files import File


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
