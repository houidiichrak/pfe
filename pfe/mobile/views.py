# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import userFormLogin, workerPos

from service.models import Worker, PositionWorker, Reservation

# Create your views here.
def index(request):
    if request.method == "POST":
        form = userFormLogin(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            try:
                w = Worker.objects.get(username=uname,password=upass)
                request.session['access'] = w.id
                return redirect('mobile:location')
            except:
                return redirect('service:notfoundpage')
    else:
        form = userFormLogin()
    return render(request, 'mobile.html' , {'form' : form})


def location(request):
	if request.method == "POST":
			form = workerPos(request.POST)
			m = PositionWorker()
			if form.is_valid():
				m.x = form.cleaned_data['lat']
				m.y = form.cleaned_data['lon']
				m.currentUser  = Worker.objects.get(id=request.session['access'])
				m.save()
				return redirect('mobile:reservation')

	else:
		form = workerPos()
	return render(request, 'locationworker.html' , {'form' : form})


def reservation(request):

    currentw  = Worker.objects.get(id=request.session['access'])
    res = Reservation.objects.filter(resworker=currentw)
    return render(request, 'reservation.html', {'res' : res})