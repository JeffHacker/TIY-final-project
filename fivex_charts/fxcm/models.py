from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    member = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return 'username: {}'.format(self.user)


class ClosedTrades(models.Model):
    user = models.ForeignKey(UserProfile)
    ticket = models.IntegerField()
    symbol = models.CharField(max_length=7)
    volume = models.IntegerField()
    opendatetime = models.DateTimeField()
    closedatetime = models.DateTimeField()
    soldprice = models.DecimalField(max_digits=None, decimal_places=5)
    boughtprice = models.DecimalField(max_digits=None, decimal_places=5)
    direction = models.CharField(max_length=5)
    grossprofitloss = models.DecimalField(max_digits=None, decimal_places=2)
    comm = models.DecimalField(max_digits=None, decimal_places=2)
    dividends = models.DecimalField(max_digits=None, decimal_places=2)
    rollover = models.DecimalField(max_digits=None, decimal_places=2)
    adj = models.DecimalField(max_digits=None, decimal_places=2)
    netprofitloss = models.DecimalField(max_digits=None, decimal_places=2)
    buycondition = models.CharField(max_length=3)
    sellcondition = models.CharField(max_length=3)
    createdbyaccount = models.IntegerField()
    journal = models.TextField()

'''
class AccountActivity(models.Model):
    timeposted = models.DateTimeField()
    code = models.CharField(max_length=10)
    description = models.TextField(max_length=100)
    account = models.IntegerField()
    ticket = models.IntegerField()
    amount = models.DecimalField(max_digits=None, decimal_places=2)
    balance = models.DecimalField(max_digits=None, decimal_places=2)
'''