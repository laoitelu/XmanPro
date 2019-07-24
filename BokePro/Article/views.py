# -*-coding:utf8-*-
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Post


# Create your views here.
def post(request):

    article = Post.objects.all()
    paginator = Paginator(article, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('index.html', locals())


def article_list(request, src):

    art_list = Post.objects.filter(id=int(src))
    return render_to_response('article.html', locals())
