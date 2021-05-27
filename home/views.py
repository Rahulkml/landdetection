from django.shortcuts import render
from home.forms import EnquiryModelForm
from home.models import Enquiry

# Create your views here.
def homepage(request):
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1
    # context = {
    #     'num_visits': num_visits,
    # }
    return render(request, 'home.html', {'nbar': 'home'})

def aboutUs(request):
    return render(request, 'about.html', {'nbar': 'about'})

def laws(request):
    return render(request, 'laws.html', {'nbar': 'laws'})

def contact(request):
    return render(request, 'contact.html', {'nbar': 'contact'})

def services(request):
    return render(request, 'services.html', {'nbar': 'services'})

# def enquiry(request):
#     return render(request, 'enquiry.html', {'nbar': 'enquiry'})

def privacy(request):
    return render(request, 'privacy.html', {'nbar': 'privacy'})

# def enquiry(request):

#     form = EnquiryForm()

#     context = {
#         'form': form,
#         'nbar': 'enquiry',
#     }

#     return render(request, 'enquiry.html', context=context)

# class AuthorCreate(CreateView):
#     model = Enquiry
#     fields = ['active', 'card_no', 'mem_name', 'land', 'district', 'land_type', 'email_id',]


def enquiry(request):

    context ={}
  
    if request.method == "POST":
        # create object of form
        form = EnquiryModelForm(request.POST)
      
        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            form.active = 1
            form.save()    
    else:
        form = EnquiryModelForm(initial={'active': 1})
        context = {
            'form': form,
            'nbar': 'enquiry',
        }
        return render(request, 'enquiry.html', context=context)
    
    form1 = EnquiryModelForm(initial={'active': 1})
    context = {
        'form': form1,
        'nbar': 'enquiry',
    }
    return render(request, 'enquiry.html', context=context)
  
    # context['form']= form
    # return render(request, "enquiry.html", context)

#dummy comment


   
   
#    if request.method == "POST":
#       #Get the posted form
#       form = EnquiryForm(request.POST)
      
#       if form.is_valid():
#          username = form.card_no
#    else:
#         form = EnquiryForm()
#         context = {
#             'form': form,
#             'nbar': 'enquiry',
#         }
#         return render(request, 'enquiry.html', context=context)
