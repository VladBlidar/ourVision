from django.shortcuts import render, redirect
from contact.forms import ContactForm
from contact.models import Message, FloaterMessage, Application
from contact.forms import FloaterForm, ApplicationForm
from django.core.mail import send_mail

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
            body = "Email: " + email + "\n\n"
            body += "Telefon: " + phone + "\n"
            send_mail(
                'Cineva doreste sa va contacteze...',
                body,
                'visionstudios.office@gmail.com',
                ['office@visionstudios.ro'],
                fail_silently=True,
            )
            send_mail(
                'Confirmare Vision Studios',
                'Mesajul dumneavoastra a fost inregistrat si veti fi contactata in curand!\n\n Toate cele bune,\n Echipa Vision Studios',
                'visionstudios.office@gmail.com',
                [email],
                fail_silently=True,
            )
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('/')

levels = [
            ('', "Nivel limbă engleză"),
            ('1', 'Începător'),
            ('2', 'Mediu'),
            ('3', 'Avansat')
          ]

experience_lv = [
            ('', "Experiență"),
            ('1', 'Nu'),
            ('2', 'Da, sub 6 luni'),
            ('3', 'Da, peste 6 luni')
          ]

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
            body = "Email: " + email + "\n\n"
            body += "Nume: " + name + "\n\n"
            body += "Mesaj: " + message
            send_mail(
                'Cineva doreste sa va contacteze...',
                body,
                'visionstudios.office@gmail.com',
                ['office@visionstudios.ro'],
                fail_silently=True,
            )
            send_mail(
                'Confirmare Vision Studios',
                'Mesajul dumneavoastra a fost inregistrat si veti fi contactata in curand!\n\n Toate cele bune,\n Echipa Vision Studios',
                'visionstudios.office@gmail.com',
                [email],
                fail_silently=True,
            )
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
            facebook = request.POST.get('facebook')
            instagram = request.POST.get('instagram')
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
                message = message,
                facebook=facebook,
                instagram=instagram,
            )
            application.save()
            body = "Nume: " + name + "\n\n"
            body += "Telefon: " + phone + "\n\n"
            body += "Anul nasterii: " + year_of_birth + "\n\n"
            body += "Nivel limba engleza: " + dict(levels)[english_level] + "\n\n"
            body += "Experienta: " + dict(experience_lv)[experience] + "\n\n"
            body += "Facebook: " + facebook + "\n\n"
            body += "Instagram: " + instagram + "\n\n"
            
            if message != "":
                body += "Mesaj: " + message

            send_mail(
                'APLICATIE NOUA',
                body,
                'visionstudios.office@gmail.com',
                ['nicu@visionstudios.ro', 'office@visionstudios.ro'],
                fail_silently=True,
            )
            # 'visionstudios.office@gmail.com',
            #     ['visionstudios.office@gmail.com'],
            return redirect ('/')

        print(appForm.errors)
        return render(request, "apply.html", {'appForm': appForm, 'flForm' : floaterForm})

