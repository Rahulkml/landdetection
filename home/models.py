from django.db import models

# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


a=u'തെങ്ങ് പ്രധാന വിളയായ ഭൂമി'
one=a.encode('utf-8').decode('utf-8')

b=u'കവുങ്ങ് പ്രധാന വിളയായ ഭൂമി'
two=b.encode('utf-8').decode('utf-8')

c=u'കുരുമുളക് പ്രധാന വിളയായ ഭൂമി'
three=c.encode('utf-8').decode('utf-8')

d=u'കശുമാവ് പ്രധാന വിളയായ ഭൂമി'
four=d.encode('utf-8').decode('utf-8')

e=u'മറ്റ് കര ഭൂമി'
five=e.encode('utf-8').decode('utf-8')

f=u'പള്ളിയാൽ ഭൂമി'
six=f.encode('utf-8').decode('utf-8')


    # card_no = forms.IntegerField()
    # mem_name = forms.CharField()
    # land = forms.FloatField()
    # district = forms.ChoiceField(choices = DISTRICT_CHOICES)
    # land_type = forms.ChoiceField(choices = LAND_CHOICE)
    # email_id = forms.EmailField()


class Enquiry(models.Model):
    """Model representing Enquiry."""
    active = models.IntegerField(max_length=1)
    card_no = models.CharField(max_length=20)
    mem_name = models.CharField(max_length=200)
    land = models.FloatField(max_length=200)

    DISTRICT_CHOICE = (
        ('AL', 'Alappuzha'),
        ('ER', 'Ernakulam'),
        ('ID', 'Idukk'),
        ('KN', 'Kannur'),
        ('KS', 'Kasaragod'),
        ('KL', 'Kollam'),
        ('KT', 'Kottayam'),
        ('KZ', 'Kozhikode'),
        ('MA', 'Malappuram'),
        ('PL', 'Palakkad'),
        ('PT', 'Pathanamthitta'),
        ('TV', 'Thiruvananthapuram'),
        ('TS', 'Thrissur'),
        ('WA', 'Wayanad'),
    )

    district = models.CharField(
        max_length=2,
        choices=DISTRICT_CHOICE,
        blank=True,
    )

    LAND_CHOICE = (
        ("a", one),
        ("b", two),
        ("c", three),
        ("d", four),
        ("e", five),
        ("f", six),
    )

    land_type = models.CharField(
        max_length=1,
        choices=LAND_CHOICE,
    )

    email_id = models.CharField(max_length=200)

    
    def __str__(self):
        """String for representing the Model object."""
        return self.card_no
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this card."""
        return reverse('card-detail', args=[str(self.id)])
