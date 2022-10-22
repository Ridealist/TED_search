from django_elasticsearch_dsl import Document
from elasticsearch_dsl import Index
from django_elasticsearch_dsl.registries import registry
from .models import Talk

talks = Index('talks')
talks.settings(number_of_shards=1, number_of_replicas=0)


@registry.register_document
@talks.document
class TalkDocument(Document):
    class Index:
        name = 'talks'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Talk

        fields = [
            'name',
            'description',
            'speaker',
            'number_of_views',
            'transcript',
        ]

# @talks.doc_type
# class TalkDocument(Document):
#     class Meta:
#         model = Talk

#         fields = (
#             'name',
#             'description',
#             'speaker',
#             'number_of_views',
#             'transcript',
#         )

