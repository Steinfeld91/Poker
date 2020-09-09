from django.db import models

class Bankroll(models.Model):
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