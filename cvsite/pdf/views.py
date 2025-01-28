from django.shortcuts import render
from .models import PersonalInfo
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        address = request.POST.get('address', "")
        phone = request.POST.get('phone', "")
        email = request.POST.get('email', "")
        summary = request.POST.get('summary', "")
        degree = request.POST.get('degree', "")
        school = request.POST.get('school', "")
        previous_work = request.POST.get('previous_work', "")
        skills = request.POST.get('skills', "")

        personal_info = PersonalInfo(
            name=name,
            email=email,
            phone=phone,
            address=address,
            summary=summary,
            degree=degree,
            school=school,
            previous_work=previous_work,
            skills=skills
        )
        personal_info.save()
    return render(request, 'pdf/accept.html')

def resume(request, id):
    personal_info = PersonalInfo.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'personal_info': personal_info})
    config = pdfkit.configuration(wkhtmltopdf=r'C:/Program Files/wkhtmltopdf/bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, options={'page-size': 'Letter', 'encoding': 'UTF-8'}, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'

    return response

def profile_list(request):
    profiles = PersonalInfo.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})
