# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import userFormRegister,userFormLogin,MessageContact,userPos,CommentaireForm
from .models import Message,Categorie,Worker,PositionClient,Commentaire, Reservation, PositionWorker

# Create your views here.
def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')
	
def region(request):
	return render(request, 'region.html')

def categorie(request):
	idville = request.GET.get('id')
	categories = Categorie.objects.all()
	return render(request, 'categorie.html', {'categories' : categories, 'idville' : idville})

def notfoundpage(request):
	return render(request, '404.html')

def register(request):
	if request.method == "POST":
			form = userFormRegister(request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				fname = form.cleaned_data['firstname']
				lname = form.cleaned_data['lastname']
				upass = form.cleaned_data['password']
				uemail = form.cleaned_data['email']
				user = User.objects.create_user(uname, uemail, upass)
				user.last_name = lname
				user.first_name = fname
				user.save()
				return redirect('service:index')
	else:
		form = userFormRegister()
	return render(request, 'register.html', {'form' : form})

def signin(request):
	if request.method == "POST":
			form = userFormLogin(request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				upass = form.cleaned_data['password']
				user = authenticate(request, username=uname, password=upass)
				if user is not None:
					login(request, user)
					return redirect('service:index')
				else:
					return redirect('service:notfoundpage')
	else:
		form = userFormLogin()
	return render(request, 'signin.html' , {'form' : form})

def logout_user(request):
	logout(request)
	return render(request, 'index.html')

def contact(request):
	if request.method == "POST":
			form = MessageContact(request.POST)
			m = Message()
			if form.is_valid():
				m.name = form.cleaned_data['name']
				m.email = form.cleaned_data['email']
				m.subject = form.cleaned_data['subject']
				m.msg = form.cleaned_data['msg']
				m.save()
				return redirect('service:index')

	else:
		form = MessageContact()
	return render(request, 'contact.html' , {'form' : form})

def listsworker(request):
	idcat = request.GET.get('id')
	idville = request.GET.get('idville')
	#workers = Worker.objects.all()
	cat = Categorie.objects.get(name=idcat)
	if idville and idville != 'None':
		workers = Worker.objects.filter(cat=cat, ville=idville)
	else:
		workers = Worker.objects.filter(cat=cat)
	return render(request,'workers.html',{'workers' : workers, 'idcat' : idcat})

def agent(request):
	idagent = request.GET.get('id')
	cagent = Worker.objects.get(id=idagent)
	if request.method == "POST":
			form = CommentaireForm(request.POST)
			m = Commentaire()
			if form.is_valid():
				m.name = request.user.username
				m.email = form.cleaned_data['email']
				m.com = form.cleaned_data['msg']
				m.resworker  = cagent
				m.save()
				return redirect('service:index')

	else:
		form = CommentaireForm()
	datacom = Commentaire.objects.filter(resworker=cagent)
	count	= Commentaire.objects.filter(resworker=cagent).count()
	return render(request, 'agent.html' , {'form' : form, 'cagent' : cagent , 'datacom' : datacom})

def reserver(request):
	if request.method == "POST":
			form = userPos(request.POST)
			m = PositionClient()
			if form.is_valid():
				print(form.cleaned_data['lat'])
				m.x = form.cleaned_data['lat']
				m.y = form.cleaned_data['lon']
				print(request.user.username)
				m.currentUser  = User.objects.get(username=request.user.username)
				m.save()
				x = Reservation.objects.last()
				x.PositionClient = PositionClient.objects.last()
				x.save()
			

				return redirect('service:index')

	else:
		rr = Reservation()
		idagent = request.GET.get('id')
		cagent = Worker.objects.get(id=idagent)	
		rr.client = User.objects.get(username=request.user.username)
		rr.posclient = PositionClient.objects.all()[1]
		rr.posworker = PositionWorker.objects.all()[1]
		#rr.date = '02/06/2019'
		rr.resworker = cagent
		rr.cat = cagent.cat
		rr.tache = "reservation"
		rr.save()
		form = userPos()
	return render(request, 'location.html' , {'form' : form})