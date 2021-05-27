from django import forms
from django.forms import ModelForm
from home.models import Enquiry
import unicodedata

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

g=u'തോട്ടവിള'
seven=g.encode('utf-8').decode('utf-8')

DISTRICT_CHOICES =(
    ("1", "Thiruvananthapuram"),
    ("2", "Kollam"),
    ("3", "Alappuzha"),
    ("4", "Pathanamthitta"),
    ("5", "Kottayam"),
    ("6", "Idukki"),
    ("7", "Ernakulam"),
    ("8", "Thrissur"),
    ("9", "Palakkad"),
    ("10", "Malappuram"),
    ("11", "Kozhikode"),
    ("12", "Wayanadu"),
    ("13", "Kannur"),
    ("14", "Kasaragod"),
)

LAND_CHOICE =(
    ("a", one),
    ("b", two),
    ("c", three),
    ("d", four),
    ("e", five),
    ("f", six),
    ("g", seven),
)

# class EnquiryForm(forms.Form):
#     card_no = forms.IntegerField()
#     mem_name = forms.CharField()
#     land = forms.FloatField()
#     district = forms.ChoiceField(choices = DISTRICT_CHOICES)
#     land_type = forms.ChoiceField(choices = LAND_CHOICE)
#     email_id = forms.EmailField()


class EnquiryModelForm(ModelForm):
    class Meta:
        model = Enquiry
        # fields = ['active', 'card_no', 'mem_name', 'land', 'district', 'land_type', 'email_id',]
        fields = "__all__"
        labels = {
            'card_no': ('Card No'),
            'mem_name': ('Member Name'),
            'land': ('Land in Acres'),
            'district': ('District'),
            'land_type': ('Type of Land'),
            'email_id': ('Email id'),
        }





