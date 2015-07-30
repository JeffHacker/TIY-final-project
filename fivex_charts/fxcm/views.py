from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import UploadedData
from .forms import UploadFileForm

# Create your views here.

def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = UploadedData(data = request.FILES['data']) #data is the FileField in my UploadedData model
            newdoc.save()
            #how to read data her in the view

    form = UploadFileForm() # A empty, unbound form  #UploadFileForm is equal to DocumentForm in the tutorial

    # Load documents for the list page
    documents = UploadedData.objects.all()

    # Render list page with the documents and the form
    return render_to_response('upload_data.html',
                              {'documents': documents, 'form': form}, context_instance=RequestContext(request))


def chart_list_view(request):  #I added this to test
    return render_to_response("charts.html", context_instance=RequestContext(request))


def hello(request):
    return render_to_response("base.html", context_instance=RequestContext(request))


