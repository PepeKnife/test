from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.category}"



class Listing(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    higher_bid_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="higher_bids_user")
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="listing_owner")
    image = models.CharField(max_length=400000, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name="listing_category")  
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="user_watchlist")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} -> {self.owner}: {self.price}"

class Comment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField(blank=True, null=True, max_length=1000)
    date =  models.DateField(default=timezone.now)
    listing = models.ForeignKey(Listing, blank=True, null=True, on_delete=models.CASCADE, related_name="listing_comment")

    def __str__(self):
        return f"User {self.user} comment {self.comment}"


class Bid(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="user_bids")
    bid = models.FloatField()
    listing = models.ForeignKey(Listing, blank=True, null=True, on_delete=models.CASCADE, related_name="listing_bid")

    def __str__(self):
        return f"{self.user} -> {self.bid}"
