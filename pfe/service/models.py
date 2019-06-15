# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    msg = models.TextField()

    def __str__(self):
        return self.email

class Categorie(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    ville = models.CharField(max_length=20)
    desc = models.TextField()
    datejoind = models.DateTimeField('date joind', auto_now_add=True, auto_now=False)
    cat = models.ForeignKey(Categorie,on_delete=models.CASCADE,)
    img = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name


class Prix(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=20)
    valeur = models.FloatField()

    def __str__(self):
        return self.name

class PositionWorker(models.Model):
    currentUser = models.ForeignKey(Worker,on_delete=models.CASCADE,)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return str(self.id) + " - position"

class PositionClient(models.Model):
    currentUser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return str(self.id) + " - position"

class Reservation(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    resworker = models.ForeignKey(Worker,on_delete=models.CASCADE,)
    posclient = models.ForeignKey(PositionClient,on_delete=models.CASCADE,)
    posworker = models.ForeignKey(PositionWorker,on_delete=models.CASCADE,)
    date = models.DateTimeField('date joind', auto_now_add=True, auto_now=False)
    cat = models.ForeignKey(Categorie,on_delete=models.CASCADE,)
    tache = models.TextField()
    is_approved = models.BooleanField(editable=False, default=False)

    def __str__(self):
        return str(self.date)

class Commentaire(models.Model):
    resworker = models.ForeignKey(Worker,on_delete=models.CASCADE,)
    com = models.TextField()
    date = models.DateTimeField('date joind', auto_now_add=True, auto_now=False)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.name