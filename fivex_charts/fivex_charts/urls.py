"""fivex_charts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import  CreateView
from django.views.generic import ListView
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from fxcm.views import upload_data, matplot_lib, logout_view
from fxcm.models import ClosedTrade

urlpatterns = [
    url(r'^$', upload_data, name='upload_data'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', logout_view, name='logout'),
    url(r'^charts/', matplot_lib, name='charts'),
    url(r'^upload_data/', upload_data, name='upload_data'),
    url(r'^register/', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url='/'), name='register'),
    url(r'^trade_list/$', ListView.as_view(model=ClosedTrade, template_name = "trade_list.html"), name='trade_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

