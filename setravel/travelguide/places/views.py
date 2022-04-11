from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Place, PlaceDetail, Images, Comments


def placelist(request):
    if 'search' in request.GET:
        search = request.GET['search'].strip()
        if search != "":
            places = Place.objects.filter(title__icontains=search)
    else:
        places = Place.objects.all().order_by('title')
    detailplaces = PlaceDetail.objects.all()
    paginator = Paginator(places, 4)
    page_number = request.GET.get('page')
    places_obj = paginator.get_page(page_number)
    context = {
        'places': places_obj,
        'detailplaces': detailplaces,
    }
    return render(request, 'places/list.html', context)


def detailplace(request, place_title):
    place = Place.objects.get(title=place_title)
    placedetail = PlaceDetail.objects.get(place=place)
    image = Images.objects.get(place=place)
    usercomment = None
    if User.is_authenticated:
        if 'userid' in request.POST:
            usercomments(request, place)
            userid = request.POST.get('userid')
            user = User.objects.get(id=userid)
            if Comments.objects.filter(user=user, place=place):
                usercomment = Comments.objects.get(user=user, place=place)
    comments = Comments.objects.filter(place=place)
    commentscount = comments.count()
    average = 0
    if commentscount != 0:
        total = 0
        for comment in comments:
            total += comment.rating
        average = total / commentscount
    context = {
        'place': place,
        'placedetail': placedetail,
        'image': image,
        'comments': comments,
        'usercomment': usercomment,
        'commentscount': commentscount,
        'average': average,
    }
    return render(request, 'places/detail.html', context)


def usercomments(request, place):
    userid = request.POST.get('userid')
    user = User.objects.get(id=userid)
    usercomment = None
    if Comments.objects.filter(user=user, place=place):
        usercomment = Comments.objects.get(user=user, place=place)
        if 'comment' in request.POST:
            comment = request.POST.get('comment').strip()
            if comment != "":
                rating = request.POST.get('rating')
                usercomment.rating = rating
                usercomment.comment = comment
                usercomment.save()
            else:
                messages.add_message(request, messages.WARNING, 'Comment is not spaces.')
        elif 'delete' in request.POST:
            usercomment.delete()
            return detailplace(request, place.title)
    else:
        if 'comment' in request.POST:
            comment = request.POST.get('comment').strip()
            if comment != "":
                rating = request.POST.get('rating')
                Comments.objects.create(place=place, rating=rating, user=user, comment=comment)
                return detailplace(request, place.title)
            else:
                messages.add_message(request, messages.WARNING, 'Comment is not spaces.')


def adding_place(request):
    if User.is_superuser:
        if request.method == 'POST':
            if 'placetitle' in request.POST:
                placetitle = request.POST.get('placetitle').strip()
                placecategory = request.POST.get('placecategory')
                placedesc = request.POST.get('placedesc').strip()
                placeregion = request.POST.get('placeregion').strip()
                placecity = request.POST.get('placecity').strip()
                placecardimage = request.FILES.get('placecardimage')
                placeimage = request.FILES.get('placeimage')
                Place.objects.create(
                    title=placetitle, cardimage=placecardimage)
                place = Place.objects.get(title=placetitle)
                PlaceDetail.objects.create(
                    place=place, name=placetitle , category=placecategory, description=placedesc, region=placeregion, city=placecity)
                Images.objects.create(place=place, image=placeimage)
                messages.add_message(request, messages.SUCCESS, 'Added place')
                return placelist(request)
            else:
                return render(request, 'places/adding_place.html')
        else:
            return render(request, 'pages/index.html')
    else:
        return render(request, 'user/login.html')


def category(request, categoryname):
    places = list()
    detailplaces = PlaceDetail.objects.filter(category=categoryname)
    if 'search' in request.GET:
        search = request.GET['search'].strip()
        if search != "":
            searchplace = Place.objects.filter(title__icontains=search)
    else:
        searchplace = Place.objects.all().order_by('title')
    for detplace in detailplaces:
        for place in searchplace:
            if detplace.name == place.title:
                places.append(place)
    paginator = Paginator(places, 4)
    page_number = request.GET.get('page')
    places_obj = paginator.get_page(page_number)
    context = {
        'places': places_obj,
        'detailplaces': detailplaces,
    }
    return render(request, 'places/list.html', context)
