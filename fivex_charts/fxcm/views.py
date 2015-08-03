import numpy as np
import pandas as pd
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import UploadedData, ClosedTrade
from .forms import UploadFileForm
from .converter import scatter_to_base64


# Create your views here.


def matplot_lib(request):
    data = UploadedData.objects.get(id=39)
    print(data.data)
    df = pd.read_csv(data.data)
    print(df.head(2))

    graph_one = scatter_to_base64(df, "ave_pl_by_symbol")
    graph_two = scatter_to_base64(df, "ave_pl_by_wkday")
    graph_three = scatter_to_base64(df, "ave_pl_by_month")
    graph_four = scatter_to_base64(df, "ave_pl_by_year")
    graph_five = scatter_to_base64(df, "ave_pl_by_direction")
    graph_six = scatter_to_base64(df, "ave_pl_by_session")
    graph_seven = scatter_to_base64(df, "ave_pl_by_dir_session")
    return render_to_response("charts.html", {"graph_one": graph_one, "graph_two": graph_two
                                              , "graph_three": graph_three, "graph_four": graph_four
                                              , "graph_five": graph_five, "graph_six": graph_six
                                              , "graph_seven": graph_seven})


def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            trade_list = list(request.FILES['data'])
            newdoc = UploadedData(data = request.FILES['data']) #data is the FileField in my UploadedData model
            newdoc.save()
            print(newdoc)
            #how to read data here in the view
            for trade in trade_list[1:]: # or data?
                cleantrade = trade.decode("utf-8") #Bekk
                print("CLEANTRADE", cleantrade)
                trade_info = cleantrade.replace("\n", "").split(',')
                print(trade_info)
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
                ClosedTrade.objects.create(data=newdoc, ticket=trade_info[0], symbol=trade_info[1], volume=trade_info[2],
                                            opendatetime=trade_info[3], closedatetime=trade_info[4], soldprice=trade_info[5],
                                            boughtprice=trade_info[6], direction=trade_info[7],
                                            grossprofitloss=trade_info[8], comm=trade_info[9], dividends=trade_info[10],
                                            rollover=trade_info[11], adj=trade_info[12], netprofitloss=trade_info[13],
                                            buycondition=trade_info[14], sellcondition=trade_info[15],
                                            createdbyaccount=trade_info[16])


    form = UploadFileForm() # A empty, unbound form  #UploadFileForm is equal to DocumentForm in the tutorial

    # Load documents for the list page
    documents = UploadedData.objects.all()


    # Render list page with the documents and the form
    return render_to_response('upload_data.html',
                              {'documents': documents, 'form': form}, context_instance=RequestContext(request))


def chart_list_view(request):  # I added this to test
    return render_to_response("charts.html", context_instance=RequestContext(request))


def hello(request):
    return render_to_response("base.html", context_instance=RequestContext(request))
