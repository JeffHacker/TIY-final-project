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


class Graph(models.Model):
    content = models.TextField()
    data = models.TextField(db_index=True)


class UploadedData(models.Model):
    data = models.FileField(upload_to='csv_data/%Y/%m/%d')
    create_time = models.DateTimeField(auto_now_add=True)


class ClosedTrade(models.Model):
    user = models.ForeignKey(User, null=True)
    data = models.ForeignKey(UploadedData)
    ticket = models.IntegerField()
    symbol = models.CharField(max_length=7)
    volume = models.IntegerField()
    opendatetime = models.DateTimeField()
    closedatetime = models.DateTimeField()
    soldprice = models.DecimalField(max_digits=10, decimal_places=5)
    boughtprice = models.DecimalField(max_digits=10, decimal_places=5)
    direction = models.CharField(max_length=5)
    grossprofitloss = models.DecimalField(max_digits=10, decimal_places=2)
    comm = models.DecimalField(max_digits=10, decimal_places=2)
    dividends = models.DecimalField(max_digits=10, decimal_places=2)
    rollover = models.DecimalField(max_digits=10, decimal_places=2)
    adj = models.DecimalField(max_digits=10, decimal_places=2)
    netprofitloss = models.DecimalField(max_digits=10, decimal_places=2)
    buycondition = models.CharField(max_length=3)
    sellcondition = models.CharField(max_length=3)
    createdbyaccount = models.BigIntegerField()


