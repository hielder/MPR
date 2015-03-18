"""
    File: urls.py
    
    Author: William J. Bosl
    Children's Hospital Boston
    300 Longwood Avenue
    Boston, MA 02115
    Email: william.bosl@childrens.harvard.edu
    Web: http://chip.org

    Copyright (C) 2011 William Bosl, Children's Hospital Boston Informatics Program (CHIP)
    http://chip.org. 

    Purpose:
    
    This file is part of a Django-based SMART application that implements
    a two-step test for medication adherence. It is intended to be used as
    a SMART web application within the context of a SMART container. See
    http://www.smarthealthit.org/ for detailed information about SMART applications.
        
    License information should go here.

    $Log: urls.py,v $
"""

from django.conf.urls.defaults import patterns
from MedCheck.views import index, launch, risk, about, choose_med, authorize
import settings

# A typical urlconf entry looks like this:
#(r'<regex>', <view_function>, <arg_dict>),


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^fhir-app/index.html$', index),
    (r'^fhir-app/launch.html$', launch),
    (r'^fhir-app/authorize.html$', authorize),
    
    # List of all patients, indicating those with potential adherence issues
    (r'^fhir-app/risk.html$', risk),
    (r'^fhir-app/about.html$', about),
    (r'^fhir-app/choose_med.html$', choose_med),
    
    # For images
    (r'^fhir-app/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    
    # For RDF-NT drug information. This is not currently used, but may be useful in the future if
	# the number of drugs/drug classes expands. To use the NDF-RT database, uncomment the 
	# settings.NDF_RT variable in settings.py
    #(r'^fhir-app/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.NDF_RT}),
        
    # Examples:
    # url(r'^$', 'SMART.views.home', name='home'),
    # url(r'^SMART/', include('SMART.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
