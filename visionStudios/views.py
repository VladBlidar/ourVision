from django.shortcuts import render, redirect
from contact.forms import ContactForm
from contact.models import Message, FloaterMessage, Application
from contact.forms import FloaterForm, ApplicationForm

def homePage(request):
    floaterForm = FloaterForm()
    return render(request, "home.html", {'flForm' : floaterForm})

def modelsPage(request):
    floaterForm = FloaterForm()
    if request.method == 'GET':
        return render(request, "models.html", {'flForm' : floaterForm})

def aboutUsPage(request):
    floaterForm = FloaterForm()
    if request.method == 'GET':
        return render(request, "aboutUs.html", {'flForm' : floaterForm})

def galeryPage(request):
    floaterForm = FloaterForm()
    if request.method == 'GET':
        return render(request, "galery.html", {'flForm' : floaterForm})

def submitFloater(request):
    if request.method == 'POST':
        form = FloaterForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            msg = FloaterMessage(
                email = email,
                phone = phone
            )
            msg.save()
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/')

def contactPage(request):
    floaterForm = FloaterForm()
    if request.method == 'GET':
        contactForm = ContactForm()
        return render(request, "contact.html", {'form': contactForm, 'flForm' : floaterForm})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            name = request.POST.get('name')
            message = request.POST.get('message')
            msg = Message(
                email = email,
                name = name,
                message = message
            )
            msg.save()
        return redirect('/')

def applyPage(request):
    floaterForm = FloaterForm()
    appForm = ApplicationForm()
    if request.method == 'GET':
        return render(request, "apply.html", {'appForm': appForm, 'flForm' : floaterForm})
    else:
        appForm = ApplicationForm(request.POST)
        if appForm.is_valid():
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            year_of_birth = request.POST.get('year_of_birth')
            english_level = request.POST.get('english_level')
            experience = request.POST.get('experience')
            if request.POST.get('message') != "Mesajul tău (opțional)":
                message = request.POST.get('message')
            else:
                message = ""
            application = Application(
                name = name,
                phone = phone,
                year_of_birth = year_of_birth,
                english_level = english_level,
                experience = experience,
                message = message
            )
            application.save()
            redirect ('/')
        return render(request, "apply.html", {'appForm': appForm, 'flForm' : floaterForm})

