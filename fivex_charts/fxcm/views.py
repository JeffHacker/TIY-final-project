from django.db import IntegrityError
import numpy as np
import pandas as pd
from .converter import scatter_to_base64
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django_pandas.io import read_frame
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from .forms import UploadFileForm
from .models import UploadedData, ClosedTrade
from numpy.random import randn

# Create your views here.


class TradeListView(ListView):
    model = ClosedTrade
    template_name = 'trade_list.html'
    def get_queryset(self):
        # Individual trades for current user
        return ClosedTrade.objects.filter(user=self.request.user)


class TradeDetailView(DetailView):
    model = ClosedTrade
    template_name = 'trade_detail.html'


def main_landing(request):
    return render_to_response('main_landing.html')


@login_required
def internal_landing(request):
    return render_to_response('internal_landing.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def matplot_lib(request):  # this creates the charts using converter.py
    context = {}
    qs = ClosedTrade.objects.filter(user=request.user)
    context['message'] = "Charts represent all dates in database.  Select 'Start' and 'End' dates to select a specific date range"
    if len(qs) == 0:
        return redirect('trade_list')
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        context['message'] = "Charts represent trade data from {} to {}".format(start_date, end_date)
        if 'start_date' == 'end_date':
            context['message'] = "Charts represent data for {}".format(start_date)
            qs = ClosedTrade.objects.filter(user=request.user, opendatetime = str(start_date))
        else:
            print(start_date, end_date)
            qs = ClosedTrade.objects.filter(user=request.user, opendatetime__range=[str(start_date), str(end_date)]) # Date filters will likely plug in here!!!!!!!
            print(qs)
            if len(qs) == 0:
                return render_to_response("charts.html", {"invalid_date_response": "These dates contain no trades" },
                                                          context_instance=RequestContext(request))
    print("QS", qs)
    df = read_frame(qs, coerce_float=True).convert_objects(convert_numeric=True, convert_dates=True)
    print(df.dtypes)
    graph_one = scatter_to_base64(df, "ave_pl_by_symbol")
    graph_two = scatter_to_base64(df, "ave_pl_by_wkday")
    graph_three = scatter_to_base64(df, "ave_pl_by_month")
    graph_four = scatter_to_base64(df, "ave_pl_by_year")
    graph_five = scatter_to_base64(df, "ave_pl_by_direction")
    graph_six = scatter_to_base64(df, "ave_pl_by_session")
    graph_seven = scatter_to_base64(df, "ave_pl_by_dir_session")
    context["graph_one"] = graph_one
    context["graph_two"] = graph_two
    context["graph_three"] = graph_three
    context["graph_four"] = graph_four
    context["graph_five"] = graph_five
    context["graph_six"] = graph_six
    context["graph_seven"] = graph_seven

    print(context)
    return render_to_response("charts.html", context, context_instance=RequestContext(request))


@login_required
def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            trade_list = list(request.FILES['data'])
            newdoc = UploadedData(user=request.user, data = request.FILES['data']) #data is the FileField in my UploadedData model
            newdoc.save()  # save file to FileField
            #print(newdoc)
            #reading in the data fields
            for trade in trade_list[1:]: # or data?
                cleantrade = trade.decode("utf-8")  # Bekk
                #print("CLEANTRADE", cleantrade)
                trade_info = cleantrade.replace("\n", "").split(',')
                #print(trade_info)
                trade_info[0] = int(trade_info[0])
                trade_info[2] = int(trade_info[2])
                trade_info[5] = float(trade_info[5])
                trade_info[6] = float(trade_info[6])
                trade_info[8] = float(trade_info[8])
                trade_info[9] = float(trade_info[9])
                trade_info[10] = float(trade_info[10])
                trade_info[11] = float(trade_info[11])
                trade_info[12] = float(trade_info[12])
                trade_info[13] = float(trade_info[13])
                trade_info[16] = int(trade_info[16])
                try:
                    ClosedTrade.objects.create(user=request.user, data=newdoc, ticket=trade_info[0], symbol=trade_info[1],
                                               volume=trade_info[2], opendatetime=trade_info[3], closedatetime=trade_info[4],
                                               soldprice=trade_info[5], boughtprice=trade_info[6], direction=trade_info[7],
                                               grossprofitloss=trade_info[8], comm=trade_info[9], dividends=trade_info[10],
                                               rollover=trade_info[11], adj=trade_info[12], netprofitloss=trade_info[13],
                                               buycondition=trade_info[14], sellcondition=trade_info[15],
                                               createdbyaccount=trade_info[16])
                except IntegrityError:
                    continue

    form = UploadFileForm() # A empty, unbound form  #UploadFileForm is equal to DocumentForm in the tutorial
    # Load documents for the list page
    documents = UploadedData.objects.all()
    # Render list page with the documents and the form
    return render_to_response('upload_data.html',
                              {'documents': documents, 'form': form}, context_instance=RequestContext(request))
