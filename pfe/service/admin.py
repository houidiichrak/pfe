# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Message,PositionWorker,Prix,Reservation,Categorie,Worker,PositionClient,Commentaire

admin.site.register(Message)
admin.site.register(PositionWorker)
admin.site.register(Prix)
admin.site.register(Reservation)
admin.site.register(Categorie)
admin.site.register(Worker)
admin.site.register(PositionClient)
admin.site.register(Commentaire)
