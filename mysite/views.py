#!/usr/bin/env python
# encoding: utf-8
"""
from /

views.py

Created by Ryan Walton on 2013-03-02.
Copyright (c) 2013 Ezdia Inc. All rights reserved.
"""
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import send_mail
from mydb.models import *
from mysite.forms import *
import sys
import os

# Main Pages

def home(request):
    return render(request, 'home.html', {"name": "home"}, )

def rsvp(request):
	return render(request, 'rsvp.html', {"name": "rsvp"}, )

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        users = Mysiteuser.objects.filter(first_name__icontains=q)
        return render(request, 'search_results.html',
            {'users': users, 'query': q})
    else:
        return render(request, 'rsvp.html', {'error': True})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'ryang24@gmail.com'),
                ['ryang24@gmail.com'],
            )
            return render(request, 'thanks.html', {"name": "thanks"}, )
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form, "name": "contact"}, )

def userform(request):
    if request.method == 'POST':
        form = MysiteuserForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return render(request, 'thanks.html', {"name": "thanks"}, )
    else:
        form = MysiteuserForm()
    return render(request, 'user_form.html', {'form': form, "name": "userform"}, )
	
	
	
	
	