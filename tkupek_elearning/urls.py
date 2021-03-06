"""tkupek_elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import tkupek_elearning.elearning.views

urlpatterns = [
    url(r'^$', tkupek_elearning.elearning.views.start),
    url(r'^admin/', admin.site.urls),
    url(r'start', tkupek_elearning.elearning.views.start),
    url(r'api', tkupek_elearning.elearning.views.get_answer),
    url(r'statistic', tkupek_elearning.elearning.views.statistic),
    url(r'^tinymce/', include('tinymce.urls')),
]

