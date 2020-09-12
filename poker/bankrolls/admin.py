from django.contrib import admin

from .models import Bankroll, Transaction

admin.site.register(Bankroll)
admin.site.register(Transaction)