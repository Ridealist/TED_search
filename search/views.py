from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from django.views.generic import TemplateView
from django.db.models import Q
from django.shortcuts import render

from search.documents import TalkDocument
from search.models import Talk

from elasticsearch import Elasticsearch

class IndexView(TemplateView):
    template_name = "talk_list.html"


def results(request):

    search_word = request.GET.get('search')
    s = TalkDocument.search().query("match", description=search_word)
    qs = s.to_queryset()

    category = Talk.objects.all()
    qs = category.filter(
        Q(name__icontains=search_word)
    )

    context = {'query': qs} #, 'query': keywords}

    return render(request, 'training_list.html', context)

class SearchView(APIView):

    def get(self, request):
        es = Elasticsearch(hosts='localhost', port=9200)

        search_word = request.query_params.get('search')

        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': "search word is missing"})
        docs = es.search(
            index='training',
            body= {
                "query": {
                    "multi_match": {
                        "query": search_word,
                        "fields": ['title', 'purpose', 'summary']
                    }
                }
            }
        )
        data_list = docs['hits']

        return Response(data_list)