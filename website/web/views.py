# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse



#from django.db import models
#from .models import Post, Comment
#from .forms import NewComment, PostCreateForm
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.views.generic import CreateView, UpdateView, DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def home(request):
    return render(request,'page1/web/index.html', {'title':'Home'},)

def page(request):
    return render(request,'page2/web/index.html',{'title':'Home'},)
    #'C:/Python27/Project_API_tweet/website/website/web/template/web/index.html',{'title':'Home'},)

# Create your views here.




    #posts = Post.objects.all()
    #paginator = Paginator(posts,1)
    #page = request.GET.get('page1')
    #try:
    #    posts = paginator.page(page)
    #except PageNotAnInteger:
    #    posts = paginator.page(1)
    #except EmptyPage:
    #    posts = paginator.page(paginator.num_page)
   # 
    #return render(request, 'web/index.html',{'title':'Home'})

