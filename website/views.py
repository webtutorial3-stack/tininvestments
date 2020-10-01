from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import render

from website.models import Setting, FAQ


def home(request):
    return render(request, 'home.html', {})


def homes(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['Modpoolsofficial69@gmail.com'],
        )

        return render(request, 'home.html', {'message_name': message_name})

    else:
        return render(request, 'home.html', {})


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'about.html', context)

def project(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'project.html', context)


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['Modpoolsofficial69@gmail.com'],
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'pricing.html', context)


def gallery(request):
    return render(request, 'gallery.html', {})


def faq(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'faq.html', context)
