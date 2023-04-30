from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Category, Comment, Listing, Bid


def index(request):
    listings = Listing.objects.filter(active=True)
    return render(request, "auctions/listing/index.html", {
        "listing": listings
    })

def createListing(request):
    if request.method == 'GET':        
               
        categories = Category.objects.all()
        return render(request, "auctions/listing/create.html",{
            "categories": categories
        })
    else:
        title = request.POST['title']
        price = float(request.POST['price'])
        imageUrl = request.POST['image']
        description = request.POST['description']
        owner = request.user
        category = Category.objects.get(category=request.POST['category'])
        created = Listing(
            name=title,
            price=price,
            owner=owner,
            image=imageUrl,
            description=description,
            category=category
        )
        created.save()
        return HttpResponseRedirect(reverse('index'))

def listing(request, id):
    object = Listing.objects.get(pk=id)    
    #Check if user requires watchlist
    user = request.user    
    #Watchlist
    watchlist = user in object.watchlist.all()
    #Comments
    comments = Comment.objects.filter(listing=object) 


    return render(request, 'auctions/listing/listing.html',{
        "object": object,
        "watchlist": watchlist,
        "comment": comments
    })

def addToWatchlist(request, id):
    user = request.user 
    listing = Listing.objects.get(pk=id)
    listing.watchlist.add(user)

    return HttpResponseRedirect(reverse('listing', args=(listing.id, )))
    

def removeFromWatchlist(request, id):
    user = request.user 
    listing = Listing.objects.get(pk=id)
    listing.watchlist.remove(user)

    return HttpResponseRedirect(reverse('listing', args=(listing.id, )))

def watchlist(request):
    user = request.user
    listings = user.user_watchlist.all()

    return render(request, "auctions/watchlist/watchlist.html", {
        "listing": listings
    })

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories/categories.html",{
        "categories": categories
    })

def listing_category(request, cat):
    category = Category.objects.get(category=cat)
    listing = Listing.objects.filter(category=category)
    return render(request, "auctions/categories/listing_category.html", {
        "cat": category,
        "listing": listing
    })

def comments(request, id):
    user = request.user
    comment = request.POST['comment']
    requiredListing = Listing.objects.get(pk=id)

    newComment = Comment(
        user=user,
        comment=comment,
        listing=requiredListing
    )
    newComment.save()
    return HttpResponseRedirect(reverse('listing', args=(requiredListing.id, )))

@login_required
def bid(request, id):
    if request.method == 'POST':
        #New bid info
        object = Listing.objects.get(pk=id)
        #Recovery info
        bid = float(request.POST['new_bid'])
        
        #Watchlst
        watchlist = request.user in object.watchlist.all()
        #Comments
        comments = Comment.objects.filter(listing=object) 

        #Validations
        if bid >= object.price:
            new_bid = Bid(
                user = request.user,
                bid = bid,
                listing=object
            )
            new_bid.save()

            if bid > object.price:
                object.higher_bid_user = request.user
                object.price = bid
                object.save()
                    
            return render(request, 'auctions/listing/listing.html',{
                "object": object,
                "watchlist": watchlist,
                "comment": comments,
                "action": True,
                "msg": "Bid placed successfuly!!"
            })
        else:
            return render(request, 'auctions/listing/listing.html',{
                "object": object,
                "watchlist": watchlist,
                "comment": comments,
                "action": True,
                "msg": "Cant make the bid!!"
            })

      

def close_listing(request, id):
    #Close the bid
    object = Listing.objects.get(pk=id)
    object.active = False
    object.save()
   
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/users/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/users/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/users/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/users/register.html")
