# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Haaaaaaaaaaaay fasoly! </h1>')


# Create your views here.
