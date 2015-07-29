from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import ClosedTrades
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.edit import FormView


# Create your views here.

class DataCreateView(CreateView):
    model = ClosedTrades
    success_url = reverse_lazy('charts.html')
    template_name = 'upload_data.html'
    fields = 'user', 'ticket', 'symbol', 'volume', 'opendatetime', 'closedatetime', 'soldprice', 'boughtprice', \
             'direction', 'grossprofitloss', 'comm', 'dividends', 'rollover', 'adj', 'netprofitloss', 'buycondition', \
             'sellcondition', 'createdbyaccount', 'journal'

'''
def data_create_view(request):
    if request.POST:
        print('hello')
    return render_to_response('upload_data.html',  context_instance=RequestContext(request))
'''