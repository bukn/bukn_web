from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login
from models import *
#from django.core.context_processors import csrf

def index(request):
    return render(request, 'lifetracer/index.html', {})

def user(request, user_id):
    if request.user.id != int(user_id):
        return HttpResponseRedirect('/')
    u = User.objects.get(id = user_id)
    up = UserProfile.objects.get(user = user_id)
    return render_to_response(
            'lifetracer/user.html', {
                'username': u.get_full_name(),
                'ndays': str(up.ndays())
                })

def ajax_login(request):
    #email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response( 'lifetracer/ajax_login', {'result': str(user.id)})
        else:
            return render_to_response( 'lifetracer/ajax_login', {'result': '-1'})
    else:
        return render_to_response( 'lifetracer/ajax_login', {'result': '0'})

def rp(request):#register page
    return render(request, 'lifetracer/rp.html', {})
