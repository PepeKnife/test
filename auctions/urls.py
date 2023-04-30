from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("create-listing/", views.createListing, name="createListing"),
    path("listing/<int:id>", views.listing, name="listing"),

    path("categories/", views.categories, name="categories"),
    path("categories/<str:cat>", views.listing_category, name="listing_category"),

    path("addWatchlist/<int:id>", views.addToWatchlist, name="addToWatchlist"),
    path("removeWatchlist/<int:id>", views.removeFromWatchlist, name="removeFromWatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),

    path("comments/<int:id>", views.comments, name="comments"),

    path("bid/<int:id>", views.bid, name="bid"),
    path("close-listing/<int:id>", views.close_listing, name="close_listing"), 

]
