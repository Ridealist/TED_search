"""
Serializer = 직렬화

파이썬 데이터를 JSON 타입의 데이터로 변환해 주는것
Django 모델로부터 뽑은 queryset, 즉 모델 인스턴스를 JSON 타입으로 바꾸는 것
-> 시리얼라이져는 응답으로 보낼 데이터의 형태를 정해주는 하나의 틀!
"""

from rest_framework import serializers
from ..models import Talk

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = (
            'name',
            'description',
            'speaker',
            'url',
            'number_of_views',
            'transcript',
        )