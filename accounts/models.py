from django.db import models
from django.contrib import auth

# Create your models here.

class Accounts(models.Model):
    """
    Model for User Accounts signing into Stock Stalker Application
    """
    market_choices = (
        ('TSX', 'Toronto Stock Exchange'),
        ('NASDAQ', 'NASDAQ'),
        ('NYSE', 'New York Stock Exchange'),
    )

    user_id = models.ForeignKey('auth.User', related_name='account_owner')
    market = models.CharField(choices=market_choices)


class History(models.Model):
    """
    Model for storing user stock search history
    """
    account = models.ForeignKey(Accounts, related_name='account_history')
    search = models.CharField(max_length=50, null=False)
