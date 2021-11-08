from django.db import models
import datetime

class Message(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60)
    name = models.CharField(max_length=60)
    message = models.CharField(max_length=5000)
    date_sent = models.DateTimeField(verbose_name='message_sent_time', auto_now=True)

    def __str__(self):
        return self.name + ", " + self.email

class FloaterMessage(models.Model):
    email = models.EmailField(verbose_name="email", max_length=60)
    phone = models.CharField(verbose_name="phone", max_length=12)

    def __str__(self):
        return self.email + ", " + self.phone

levels = [
            ('1', 'Începător'),
            ('2', 'Mediu'),
            ('3', 'Avansat')
          ]

experience = [
            ('1', 'Nu'),
            ('2', 'Da, sub 6 luni'),
            ('3', 'Da, peste 6 luni')
          ]
            # ('0', 'Nivel limbă engleză')
class Application(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    year_of_birth = models.CharField(max_length=4)
    english_level = models.CharField(max_length=20, choices=levels)
    experience = models.CharField(max_length=20, choices=experience)
    message = models.CharField(max_length=5000, null=True, blank=True)
    facebook = models.CharField(max_length=5000, default='N/A')
    instagram = models.CharField(max_length=5000, default='N/A')
    date_sent = models.DateTimeField(verbose_name='application_sent_time', auto_now=True)
    
    def __str__(self):
        hrs = datetime.timedelta(hours = 3)
        ro_timezone = self.date_sent + hrs
        time_string = ro_timezone.strftime("%d/%m/%Y at %H:%M")
        return self.name + ", " + self.phone + ", " + time_string
