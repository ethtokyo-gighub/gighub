from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=255, unique=True) # wallet address
    signature = models.CharField(max_length=255, blank=True) # signature
    date_joined = models.DateTimeField(auto_now=True, blank=True) # date joined
    wage = models.FloatField(default=5000, blank=True)
    next_paycheck_date = models.DateTimeField(auto_now=True, blank=True) 
    last_paycheck_date = models.DateTimeField(auto_now=True, blank=True) 
    is_whitelisted = models.BooleanField(default=False) # status check if whitelisted
    orgs = models.ManyToManyField('Organization', related_name='org')  # workers

    def __str__(self):
        return self.username + " / " + self.address


class Organization(models.Model):
    title = models.CharField(max_length=255, unique=True)
    TYPE_CHOICES = [
        ('DAO', 'DAO'),
        ('Co', 'Co'),
        ('FDN', 'Foundation'),
    ]
    type_field = models.CharField(max_length=10, choices=TYPE_CHOICES) # organization type
    workers = models.ManyToManyField('User', related_name='workers')  # workers

    def __str__(self):
        return self.title

class Loan(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    org_title = models.ForeignKey('Organization', on_delete=models.CASCADE)
    next_paycheck_date = models.DateTimeField(auto_now=True, blank=True)
    token = models.CharField(default='ETH', max_length=255)  
    borrowing_amount = models.FloatField(default=0, blank=True)
    repayment_date = models.DateTimeField(auto_now=True, blank=True)
    # acccrued_interests = models.FloatField() #interest
    is_payed = models.BooleanField(default=False) #status check if payed
    LTV = models.FloatField(default=30) #loan to value
    APR = models.FloatField(default=20)
    accrued_interest = models.FloatField(default=0, blank = True)
    # loan_date = models.DateTimeField(default=datetime.now, blank=True)
    max_borrowing_amount = models.FloatField(default=0, blank=True)

    def __str__(self):
        return "user: " + self.user.address[:5] + " / org: " + self.org_title.title + " / amount: " + str(self.borrowing_amount)
