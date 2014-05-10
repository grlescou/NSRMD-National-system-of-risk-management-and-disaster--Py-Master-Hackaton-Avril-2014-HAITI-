from android_root.forms import LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import RequestContext


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            #if user.is_superuser:
             #   return HttpResponse("Super")
            #else:
            #return HttpResponse(request.user)
        return HttpResponse(form.clean())


