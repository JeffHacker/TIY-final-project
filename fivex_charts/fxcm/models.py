from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    member = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return 'username: {}'.format(self.user)


class Graph(models.Model):
    content = models.TextField()
    data = models.TextField(db_index=True)


class UploadedData(models.Model):
    user = models.ForeignKey(User)
    data = models.FileField(upload_to='csv_data/%Y/%m/%d')
    create_time = models.DateTimeField(auto_now_add=True)


class ClosedTrade(models.Model):
    user = models.ForeignKey(User)
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

    class Meta:
        unique_together = ("user", "ticket")

    def __str__(self):
        return "Ticket:{}   Pair:{}   Volume:{}   Open Date/Time:{}   Close Date/Time:{}   Sell Price:{}   Buy Price:{} " \
               "  Dir:{}   Gross P/L:{}   Commision:{}   Dividends:{}   Rollover:{}   Adjust:{}   Net P/L:{}   Buy Cond:{}  " \
               " Sell Cond{}   Acct:{}".format(self.ticket, self.symbol, self.volume, self.opendatetime, self.closedatetime,
                                               self.soldprice, self.boughtprice, self.direction, self.grossprofitloss,
                                               self.comm, self.dividends, self.rollover, self.adj, self.netprofitloss,
                                               self.buycondition, self.sellcondition, self.createdbyaccount)


class TradeNotes(models.Model):
    trade = models.ForeignKey(ClosedTrade, related_name='tradenotes')
    note = models.TextField(blank=True, help_text='Trade Notes:')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}, {}".format(self.timestamp, self.trade)