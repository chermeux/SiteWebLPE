from datetime import datetime
from django.core.files.temp import NamedTemporaryFile

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

def loginPage(request):
    logout(request)
    if request.method == 'GET':
        if 'next' in request.GET:
            next = request.GET['next']
        else:
            next = '/'
        return render(request, 'User/login.html', {'next': next})
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    next = request.POST['next']
    if user is not None:
        login(request, user)
        return redirect(next)
    else:
        return render(request, 'User/login.html',
                      {'next': next, 'msg': 'Utilisateur ou mots de passe invalide', 'user': request.POST['user']})
