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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from fxcm.views import upload_data, chart_list_view, hello


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', upload_data, name='uploaod_data'),
    url(r'^hello/', hello, name='hello'),
    url(r'^upload_data/', upload_data, name='upload_data'),
    url(r'^charts/', chart_list_view, name='charts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
