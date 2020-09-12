#f
#from django.db import models
from djongo import models
from django.contrib.auth.models import User

class Bankroll(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=50)
    starting_balance = models.DecimalField(default=0, decimal_places=2, max_digits=50)
    created_dttm = models.DateField('date created')

    #def __str__(self):
    #    return self.bankroll_text

class Transaction(models.Model):
    bankroll = models.ForeignKey(Bankroll, on_delete=models.CASCADE)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=50)
    trans_type = models.CharField(max_length=200)
    created_dttm = models.DateField('date created')

    #def __str__(self):
    #    return self.transaction_text

class Session(models.Model):
    bankroll = models.ForeignKey(Bankroll, on_delete=models.CASCADE)
    start_dttm = models.DateTimeField()
    end_dttm = models.DateTimeField()
    buy_in = models.DecimalField(default=0, decimal_places=2, max_digits=50)
    cash_out = models.DecimalField(default=0, decimal_places=2, max_digits=50)
    notes = models.TextField(max_length=500, blank=True)
    max_table_size = models.IntegerField(default=0)
    transactions = models.ArrayReferenceField(
        to=Transaction,
        on_delete=models.CASCADE,
    )
    session_type = models.CharField(max_length=32)
    