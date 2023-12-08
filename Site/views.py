import os
import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Class, Artist, Teacher, Artwork, MailList

# Create your views here.


def index(request):
    return render(request, "Site/index.html")


def about(request):
    return render(request, "Site/about.html")


def classes(request):

    teacher_objects = Teacher.objects.all()
    teachers = []

    for t in teacher_objects:
        teacher = {}
        teacher['artist'] = t.artist
        teacher['photo'] = t.photo
        teacher['photo_size'] = t.photo_size
        teacher['quote'] = t.quote.split('--')[0]
        teacher['quote_author'] = t.quote.split('--')[1]
        teacher['started'] = t.started
        teacher['about'] = t.about.split('\r\n')
        teacher['classes'] = {}

        classes = t.get_teacher_classes()
        for c in classes:
            if teacher['classes'].get(c.group) == None:
                teacher['classes'][c.group] = {c.day : c.time}
            elif teacher['classes'][c.group].get(c.day) == None:
                teacher['classes'][c.group][c.day] = c.time

        teachers.append(teacher)
    
    return render(request, "Site/classes.html", {
        "teachers" : teachers,
    })


def exhibition(request):

    paintings = Artwork.objects.all()

    return render(request, "Site/exhibition.html", {
        "paintings" : paintings,
    })


def news_events(request):
    return render(request, "Site/news_events.html")


def contact(request):
    return render(request, "Site/contact.html")


def join(request):
    return render(request, "Site/join.html")


def privacy_policy(request):
    return render(request, "Site/privacy_policy.html")




def teacher_profile(request, teacher_id):
    t = Teacher.objects.get(artist=Artist.objects.get(pk=teacher_id))

    teacher = {}
    teacher['artist'] = t.artist
    teacher['photo'] = t.photo
    teacher['about'] = t.about.split('\r\n')
    teacher['classes'] = {}

    classes = t.get_teacher_classes()
    for c in classes:
        if teacher['classes'].get(c.group) == None:
            teacher['classes'][c.group] = []
            teacher['classes'][c.group].append(f"{c.day} : {c.time}")
        elif teacher['classes'][c.group].count(f"{c.day} : {c.time}") == 0:
            teacher['classes'][c.group].append(f"{c.day} : {c.time}")

    return render(request, "Site/teacher_profile.html", {
        "teacher" : teacher,
    })



@csrf_exempt
def contact_mail(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # send Art Alive email:
        contact_body_path = settings.BASE_DIR / "Site" / "templates" / "Site" / "contact_template.html"
        body = render_to_string(contact_body_path, {
            'name' : data['name'],
            'email' : data['email'],
            'phone' : data['phone'],
            'message' : data['message'],
        })
        email = EmailMessage(
            f"New Contact From Site {data['name']}",
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER,],
            reply_to=[data['email'],],
        )
        contact_email_sent = email.send()
        
        # send contacter email:
        if contact_email_sent != 0:
            contacter_body_path = settings.BASE_DIR / "Site" / "templates" / "Site" / "contacter_template.html"
            body = render_to_string(contacter_body_path, {
                'name' : data['name']
            })
            email = EmailMessage(
                f"Contact Recieved from Art Alive Art School",
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER,],
                reply_to=[settings.EMAIL_HOST_USER,],
            )
            email.send()

        elif contact_email_sent == 0:
            return JsonResponse("An error occurred, please try again later.", safe=False)

    return JsonResponse("Thank you for contacting us, you'll hear from us soon", safe=False)


@csrf_exempt
def subscribe(request):
    if request.method == "POST":
        data = json.loads(request.body)
        subscription = MailList(
            name = data['name'],
            email = data['email'],
            events = data['events'],
            newsletter = data['newsletter'],
        )
        subscription.save()
        return JsonResponse("", safe=False)




def painting_data(request, painting_id):
    artist_email = Artwork.objects.get(pk=painting_id).artist.email

    return JsonResponse(artist_email, safe=False)




def join_form(request):
    
    print("join form submitted")

    if request.method == "POST":
        status = generate_pdf(request)
        if status[1] == "fail":
            return render(request, "Site/join.html", {
                "message" : status[0]
            })
        elif status[1] == "success":
            status[0]
            return render(request, "Site/join.html", {
                "message" : "Thank you for submitting this form, you will hear back from us soon."
            })
    else:
        return render(request, "Site/join.html")


def generate_pdf(request):
    html_template = get_template('Site/join_pdf.html')
    
    logo_url = settings.BASE_DIR / "Site" / "static" / "resources" / "logo.png"
    id_copy = handle_uploaded_file(request.FILES['id_copy'], request.POST['name_surname'])
    signature = handle_uploaded_file(request.FILES['signature'], request.POST['name_surname'])
    context = {
        'form_data': request.POST,
        'logo_src': logo_url,
        'id_copy': id_copy,
        'signature': signature,
    }
    html_content = html_template.render(context)

    pdf = HttpResponse(content_type='application/pdf')
    pdf['Content-Disposition'] = 'attachment; filename="output.pdf"'

    # Create a PDF
    pisa_status = pisa.CreatePDF(html_content, dest=pdf)
    if not pisa_status.err:
        pdf_file_path = settings.BASE_DIR / "Site" / "static" / "upload" / f"{request.POST['name_surname']}__output.pdf"
        with open(pdf_file_path, 'wb') as pdf_file:
            pdf_file.write(pdf.content)
        join_email_sent = email_join(pdf_file_path, id_copy, request.POST['name_surname'], request.POST['email'])
        if join_email_sent == 0:
            # delete_saved_id(id_copy)
            return ["An error ocurred, please try again later.", "fail"]
        return [pdf, "success"]
    else:
        return ["An error ocurred, please try again later.", "fail"]
        


def handle_uploaded_file(f, p):
    with open('Site/static/upload/'+p+'__'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return settings.BASE_DIR / "Site" / "static" / "upload" / f"{p}__{f.name}"


def email_join(pdf_path, id_path, app_name, app_email):
    # email Art Alive:
    email = EmailMessage(
        f"New Application to Join Art Alive Art School",
        f"Dear Art Alive, \n\n You have recieved a new application to join Art Alive Art School, please see attatced PDF.",
        settings.DEFAULT_FROM_EMAIL,
        [settings.EMAIL_HOST_USER,],
    )
    email.attach_file(pdf_path)
    email.attach_file(id_path)
    join_email_sent = email.send()
    # email user:
    if join_email_sent != 0:
        email = EmailMessage(
            f"Application to Join Art Alive Art School Recieved",
            f"Dear {app_name}, \n\n we have recieved your application to join Art Alive Art School, you will hear from us soon. \n\n Your application is attatced as a PDF.",
            settings.DEFAULT_FROM_EMAIL,
            [app_email,],
        )
        email.attach_file(pdf_path)
        join_email_sent = email.send()
    else:
        return 0
