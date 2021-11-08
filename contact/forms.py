from django.forms.models import ModelForm
from django import forms
from .models import Message, FloaterMessage, Application
from django.core.exceptions import ValidationError


class ContactForm(ModelForm):
    email = forms.EmailField(label='Email', max_length=60)
    name = forms.CharField(label='Nume', max_length=60)
    message = forms.CharField(widget=forms.Textarea, max_length=3000, label='Mesajul tău')

    class Meta:
        model = Message
        fields = ['email', 'name', 'message']


class FloaterForm(ModelForm):
    email = forms.EmailField(label='Email', max_length=60)
    phone = forms.CharField(label='Telefon', max_length=15)

    class Meta:
        model = FloaterMessage
        fields = ['email', 'phone']

levels = [
            ('', "Nivel limbă engleză"),
            ('1', 'Începător'),
            ('2', 'Mediu'),
            ('3', 'Avansat')
          ]

experience = [
            ('', "Experiență"),
            ('1', 'Nu'),
            ('2', 'Da, sub 6 luni'),
            ('3', 'Da, peste 6 luni')
          ]

class ApplicationForm(ModelForm):
    name = forms.CharField(max_length=60, label=False)
    phone = forms.CharField(max_length=15, label=False)
    year_of_birth = forms.CharField(max_length=4, label=False)
    english_level = forms.ChoiceField(choices=levels, label=False)
    english_level.widget.attrs.update({'class': 'form-select'})
    experience = forms.ChoiceField(choices=experience, label=False)
    experience.widget.attrs.update({'class': 'form-select'})
    message = forms.CharField(widget=forms.Textarea, max_length=3000, label=False)
    facebook = forms.CharField(max_length=5000, label=False)
    instagram = forms.CharField(max_length=5000, label=False)

    class Meta:
        model = Application
        fields = ['name', 'phone', 'year_of_birth', 'english_level', 'experience', 'facebook', 'instagram', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Nume, prenume':
            raise ValidationError("Please input a name")
        return name
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone == 'Telefon':
            raise ValidationError("Please input a phone number")
        return phone
    
    def clean_year_of_birth(self):
        year_of_birth = self.cleaned_data.get('year_of_birth')
        if year_of_birth == 'Anul nașterii':
            raise ValidationError("Please input your year of birth")
        return year_of_birth

    def clean_facebook(self):
        facebook = self.cleaned_data.get('facebook')
        if facebook == 'N/A' or facebook == "" or facebook == 'Profil Facebook':
            raise ValidationError("Please enter your facebook")
        return facebook
    
    def clean_instagram(self):
        instagram = self.cleaned_data.get('instagram')
        if instagram == 'N/A' or instagram == "" or instagram == 'Profil Instagram':
            raise ValidationError("Please enter your instagram")
        return instagram