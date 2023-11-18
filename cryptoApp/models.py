# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    id_or_photo = models.FileField(upload_to='id_photos/', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)


class Coin(models.Model):
    name = models.CharField(max_length=250, null=True)
    symbol = models.CharField(max_length=10, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    percentage_change_1h = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    percentage_change_24h = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    percentage_change_7d = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    all_time_high = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    graph_link = models.URLField(blank=True)
    icon_url = models.URLField(blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class CurrencyConverter(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(max_length=3)
    result = models.FloatField()
    is_coin_to_currency = models.BooleanField()

    def __str__(self):
        return f"{self.amount} {self.coin.symbol} to {self.currency}"


class SocialsProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)  # one user will have only onle profile
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)
    # one user can follow many profiles - ManyToManyField
    # related_name - will be using this later for search query
    # symmetrical -  False -  so that if I follow someone they don't have to necessarily follow me
    # blank=True - this means that if i want to I don't have to follow anyone
