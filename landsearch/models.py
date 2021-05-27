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


class RationCard(models.Model):
    """Model representing a RationCard."""
    card_no = models.CharField(max_length=20)
    house_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pin_no = models.IntegerField()
    taluk = models.CharField(max_length=100)

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
        help_text='Select the district',
    )
    
    CARD_STATUS = (
        ('y', 'Yellow Card'),
        ('p', 'Pink Card'),
        ('b', 'Blue Card'),
        ('w', 'White Card'),
    )

    # Yellow Card - Most economically backward section of society. Antyodaya Anna Yojana Beneficiaries
    # Pink Card - Priority or Below Poverty Line (BPL)
    # Blue Card - Non – Priority subsidy or Above Poverty Line (APL)
    # White Card - Non – Priority

    Card_Type = models.CharField(
        max_length=1,
        choices=CARD_STATUS,
        blank=True,
        default='w',
        help_text='The type of the card',
    )
    
    def __str__(self):
        """String for representing the Model object."""
        return self.card_no
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this card."""
        return reverse('card-detail', args=[str(self.id)])


class FamMember(models.Model):
    """Model representing an family members."""
    card = models.ForeignKey('RationCard', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)

    CIVIL_STATUS = (
        ('s', 'Single'),
        ('m', 'Married'),
    )

    maritial_status = models.CharField(
        max_length=1,
        choices=CIVIL_STATUS,
        help_text='Choose your maritial status.',
    )
    
    relation = models.CharField(max_length=100)
    age = models.IntegerField()
    job = models.CharField(max_length=100)
    income = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular member instance."""
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name + ' | Card No : ' + self.card.card_no

class RevenueDetail(models.Model):
    """Model representing Revenue Details."""
    name = models.ForeignKey('FamMember', on_delete=models.SET_NULL, null=True)

    land = models.FloatField()

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
        help_text='Select the district',
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
        help_text='Select the type of land.',
    )

    def get_absolute_url(self):
        """Returns the url to access a particular member instance."""
        return reverse('revenue-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name.name


class LookUp(models.Model):
    """Model representing an revenue lookup."""
    district = models.CharField(max_length=100)

    a = models.FloatField()

    b = models.FloatField()

    c = models.FloatField()

    d = models.FloatField()

    e = models.FloatField()

    f = models.FloatField()


    def get_absolute_url(self):
        """Returns the url to access a particular member instance."""
        return reverse('lookup', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.district

