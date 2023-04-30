from django.contrib import admin
from .models import User, Category, Comment, Listing, Bid

# Register your models here.

class AdminListing(admin.ModelAdmin):
    list_display = ("id", "name", "price", "owner", "active")

class AdminComment(admin.ModelAdmin):
    list_display = ("id", "user", "comment", "listing")

class AdminBid(admin.ModelAdmin):
    list_display = ("id", "user", "bid", "listing")


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment, AdminComment)
admin.site.register(Bid, AdminBid)
admin.site.register(Listing, AdminListing)
