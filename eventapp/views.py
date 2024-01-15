from django.conf import settings
from django.shortcuts import render,redirect
from . models import Event,Contact
from . forms import BookingForm
from django.contrib import messages
import smtplib

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def events(request):
    dict_eve={'eve': Event.objects.all}
    return render(request, 'events.html',dict_eve)


def eve_detail(request, id):
    detail={'event': Event.objects.get(id=id)}
    return render(request, "event_detail.html",detail)

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form

    }
    return render(request, 'booking.html',dict_form)


def contact(request):

    if request.method == "POST":
        contact: Contact = Contact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get('message')

        contact.c_name = name
        contact.c_email = email
        contact.c_subject = message
        hello=contact.save()
        email_from=settings.EMAIL_HOST_USER
        passw=settings.EMAIL_HOST_PASSWORD
        recipient_list=contact.c_email
        message="Thanks for contact us,We will call you soon"
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
            server.login(email_from,passw)
            server.sendmail(recipient_list,email_from,message)
            server.quit()
            messages.success(request, 'Submission successful')
        return redirect('contact.html')
    return render(request, "contact.html")


