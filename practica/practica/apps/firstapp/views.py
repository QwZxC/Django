from django.shortcuts import render
from .models import Article
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics
from .serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'firstapp/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'firstapp/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('detail', args=(a.id,)))


class ArticlesAPIView(APIView):

    def post(self, request):
        article_new = Article.objects.create(title=request.data['title'],
                                             text=request.data['text'],
                                            )
        return Response({'post': model_to_dict(article_new)})

    def get(self, request):
        lst = Article.objects.all().values()
        return Response({'Post': list(lst)})



# class ArticlesAPIView(generics.ListAPIView):
#    queryset = Article.objects.all()
#    serializer_class = ArticleSerializer
