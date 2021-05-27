from landsearch.models import RationCard, FamMember, RevenueDetail, LookUp
from home.models import Enquiry
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import EligibilityForm

# Create your views here.

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

def landtype(type_para):
    if type_para == 'a':
        return one
    elif type_para == 'b':
        return two
    elif type_para == 'c':
        return three
    elif type_para == 'd':
        return four
    elif type_para == 'e':
        return five
    elif type_para == 'f':
        return six
    else:
        return seven

def count():
    count = enquiry_count = Enquiry.objects.filter(active=1).count()
    return count

# def homepage(request):
#     # num_visits = request.session.get('num_visits', 0)
#     # request.session['num_visits'] = num_visits + 1
#     # context = {
#     #     'num_visits': num_visits,
#     # }
#     return render(request, 'home.html')

@login_required
def index(request):
    """View function for home page of site."""

    enquiry_count = Enquiry.objects.filter(active=1).count()
    # Generate counts of some of the main objects
    num_cards = RationCard.objects.all().count()
    num_members = FamMember.objects.all().count()
    
    #Cards with clr yellow (Card_Type = 'y')
    num_cards_yellow = RationCard.objects.filter(Card_Type='y').count()
    
    #Cards with clr Pink (Card_Type = 'p')
    num_cards_pink = RationCard.objects.filter(Card_Type='p').count()

    #Cards with clr Blue (Card_Type = 'b')
    num_cards_blue = RationCard.objects.filter(Card_Type='b').count()

    #Cards with clr White (Card_Type = 'w')
    num_cards_white = RationCard.objects.filter(Card_Type='w').count()
    
    context = {
        'num_cards': num_cards,
        'num_members': num_members,
        'num_cards_yellow': num_cards_yellow,
        'num_cards_pink': num_cards_pink,
        'num_cards_blue': num_cards_blue,
        'num_cards_white': num_cards_white,
        'nbar': 'dashboard',
        'enquiry_count': enquiry_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# class CardListView(LoginRequiredMixin, generic.ListView):
#     paginate_by = 10
#     model = RationCard

class CardDetailView(LoginRequiredMixin, generic.DetailView):
    model = RationCard
    enquiry_count = Enquiry.objects.filter(active=1).count()
    extra_context={'enquiry_count': enquiry_count,}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enquiry_count'] = Enquiry.objects.filter(active=1).count()
        return context
    def card_detail_view(request, primary_key):
        try:
            card = RationCard.objects.get(pk=primary_key)
        except RationCard.DoesNotExist:
            raise Http404('Card does not exist')

# class CustomerListView(LoginRequiredMixin, generic.ListView):
#     paginate_by = 10
#     model = FamMember

class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = FamMember
    enquiry_count = Enquiry.objects.filter(active=1).count()
    extra_context={'enquiry_count': enquiry_count,}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enquiry_count'] = Enquiry.objects.filter(active=1).count()
        return context
    def customer_detail_view(request, primary_key):
        try:
            customer = FamMember.objects.get(pk=primary_key)
        except FamMember.DoesNotExist:
            raise Http404('Customer does not exist')

class RevenueListView(LoginRequiredMixin, generic.ListView):
    # paginate_by = 10
    template = 'landsearch/revenuedetail_list.html'
    model = RevenueDetail
    enquiry_count = Enquiry.objects.filter(active=1).count()
    extra_context={'enquiry_count': enquiry_count,}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enquiry_count'] = Enquiry.objects.filter(active=1).count()
        return context


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return redirect('/')


@login_required
def card_list(request):
    ctx = {}
    enquiry_count = Enquiry.objects.filter(active=1).count()
    url_parameter = request.GET.get("q")

    if url_parameter:
        cards = RationCard.objects.filter(card_no__icontains=url_parameter)

    else:
        cards = RationCard.objects.all()

    c = { 'cards': cards, 'nbar': 'card', 'enquiry_count': enquiry_count,}

    ctx["c"] = c
    if request.is_ajax():

        html = render_to_string(
            template_name="list/card-results-partial.html", context={"c": c}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "list/card_list.html", context=ctx)


@login_required
def member_list(request):
    ctx = {}
    enquiry_count = Enquiry.objects.filter(active=1).count()
    url_parameter = request.GET.get("q")

    if url_parameter:
        customers = FamMember.objects.filter(name__icontains=url_parameter)

    else:
        customers = FamMember.objects.all()

    c = { 'customers': customers, 'nbar': 'member', 'enquiry_count': enquiry_count, }

    ctx["c"] = c
    if request.is_ajax():

        html = render_to_string(
            template_name="list/member-results-partial.html", context={"c": c}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "list/member_list.html", context=ctx)


@login_required
def search_view(request):
    ctx = {}
    enquiry_count = Enquiry.objects.filter(active=1).count()
    url_parameter = request.GET.get("q")

    if url_parameter:
        customers = FamMember.objects.filter(card__card_no__icontains=url_parameter)
        cards = RationCard.objects.filter(card_no__icontains=url_parameter)
        # customers = FamMember.objects.filter(card__card_no__startswith=url_parameter)
        # cards = RationCard.objects.filter(card_no__startswith=url_parameter)

    else:
        customers = FamMember.objects.all()
        cards = RationCard.objects.all()

    c = { 'customers': customers, 'cards': cards, 'nbar': 'search', 'enquiry_count': enquiry_count,}

    ctx["c"] = c
    if request.is_ajax():

        html = render_to_string(
            template_name="cards-results-partial.html", context={"c": c}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "cards.html", context=ctx)


@login_required
def land_search(request, pk):
    member = FamMember.objects.get(id=pk)
    revenuedetails = RevenueDetail.objects.filter(name_id=pk)
    enquiry_count = Enquiry.objects.filter(active=1).count()

    form = EligibilityForm()
    name = member.name

    context = {
        'name': name,
        'pk': pk,
        'revenuedetails': revenuedetails,
        'form': form,
        'enquiry_count': enquiry_count,
    }

    return render(request, 'find.html', context=context)

@login_required
def verify_view(request):
    enquiry_count = Enquiry.objects.filter(active=1).count()
    if request.POST:
        land = request.POST['land']
        district = request.POST['district']
        land_type = request.POST['land_type']
        pk = request.POST['pk']
        # is_paddy = request.POST.get('is_paddy', False)

        member = FamMember.objects.get(id=pk)
        name = member.name

        if land_type == 'g':
            message = 'You have to contact the Department office for further proceedings!!!'
            context = {
                'message': message,
                'name': name,
                'enquiry_count': enquiry_count,
            }
            return render(request, 'verify.html', context=context)
        
        lookup = LookUp.objects.get(id=district)

        # if land_type == 'a':
        #     buy_absolute_value = float(land)/lookup.a
        #     # print(buy_absolute_value)
        # elif land_type == 'b':
        #     buy_absolute_value = float(land)/lookup.b
        #     # print(buy_absolute_value)
        # elif land_type == 'c':
        #     buy_absolute_value = float(land)/lookup.c
        #     # print(buy_absolute_value)
        # elif land_type == 'd':
        #     buy_absolute_value = float(land)/lookup.d
        #     # print(buy_absolute_value)
        # elif land_type == 'e':
        #     buy_absolute_value = float(land)/lookup.e
        #     # print(buy_absolute_value)
        # else:
        #     buy_absolute_value = float(land)/lookup.f
        #     # print(buy_absolute_value)

        def abs_calc(type_val, land_val ,lookup_fun):
            if type_val == 'a':
                absolute_value = float(land_val)/lookup_fun.a
                return absolute_value
            elif type_val == 'b':
                absolute_value = float(land_val)/lookup_fun.b
                return absolute_value
            elif type_val == 'c':
                absolute_value = float(land_val)/lookup_fun.c
                return absolute_value
            elif type_val == 'd':
                absolute_value = float(land_val)/lookup_fun.d
                return absolute_value
            elif type_val == 'e':
                absolute_value = float(land_val)/lookup_fun.e
                return absolute_value
            else:
                absolute_value = float(land_val)/lookup_fun.f
                return absolute_value

        buy_absolute_value = abs_calc(land_type, land, lookup)
        
        current_absolute_value = 0.0

        # for revenuedetail in revenuedetails:
        #     district_value = revenuedetail.get_district_display()
        #     land_value = revenuedetail.land
        #     land_type_value = revenuedetail.land_type
        #     lookup_a = LookUp.objects.get(district=district_value)
        #     current_absolute_value = current_absolute_value + abs_calc(land_type_value, land_value, lookup_a)
        
        def rev_diff_mem(id_value):
            current_absolute_value_a = 0.0
            revenuedetails = RevenueDetail.objects.filter(name_id=id_value)

            for revenuedetail in revenuedetails:
                district_value = revenuedetail.get_district_display()
                land_value = revenuedetail.land
                land_type_value = revenuedetail.land_type
                lookup_a = LookUp.objects.get(district=district_value)
                current_absolute_value_a = current_absolute_value_a + abs_calc(land_type_value, land_value, lookup_a)
            return current_absolute_value_a
        

        card_no = member.card.card_no

        members = FamMember.objects.all()
        mem_count = 0
        for member_a in members:
            if member_a.card.card_no == card_no:
                mem_count = mem_count + 1
                fam_mem_id = member_a.id
                current_absolute_value = current_absolute_value + rev_diff_mem(fam_mem_id)


        if mem_count == 1:
            if current_absolute_value + buy_absolute_value <= 5:
                flag = 1
            else:
                flag = 0
        elif mem_count>1 and mem_count<=5:
            if current_absolute_value + buy_absolute_value <= 10:
                flag = 1
            else:
                flag = 0
        else:
            if (current_absolute_value + buy_absolute_value) <= (10 + mem_count-5):
                flag = 1
            else:
                flag = 0

        land_type_pass = landtype(land_type)

        context = {
            'land': land,
            'flag': flag,
            'land_type_pass': land_type_pass,
            'name': name,
            'enquiry_count': enquiry_count,
        }

        return render(request, 'verify.html', context=context)
    
@login_required
def land_search(request, pk):
    member = FamMember.objects.get(id=pk)
    revenuedetails = RevenueDetail.objects.filter(name_id=pk)
    enquiry_count = Enquiry.objects.filter(active=1).count()

    form = EligibilityForm()
    name = member.name

    context = {
        'name': name,
        'pk': pk,
        'revenuedetails': revenuedetails,
        'form': form,
        'enquiry_count': enquiry_count,
    }

    return render(request, 'find.html', context=context)


@login_required
def notification_view(request):
    enquiry_count = Enquiry.objects.filter(active=1).count()
    enquiry = Enquiry.objects.filter(active=1)

    context = {
        'nbar': 'notification',
        'enquiry': enquiry,
        'enquiry_count':enquiry_count,
    }

    return render(request, 'notification.html', context=context)


@login_required
def disable(request, pk):
    Enquiry.objects.filter(id=pk).update(active=0)
    return redirect(notification_view)