from django.contrib import admin

from .models import Bankroll, Transaction, Session

admin.site.register(Bankroll)
admin.site.register(Transaction)
admin.site.register(Session)