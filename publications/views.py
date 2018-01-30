from django.shortcuts import render
from django.contrib import auth
from .models import PublicationImage


def news(request):

    publications_images = PublicationImage.objects.filter(is_active=True, publication__is_active=True)
    username = auth.get_user(request).username
    return render(request, 'publications/news.html', locals())


def articles(request):

    publications_images = PublicationImage.objects.filter(is_active=True, publication__is_active=True)
    username = auth.get_user(request).username
    return render(request, 'publications/articles.html', locals())


# Create your views here.
