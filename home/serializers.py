from rest_framework import serializers
from home.models import NewData

# 뉴스기사 모델 시리얼라이저
class NewsSerializer(serializers.Serializer):
    class Meta:
        model = NewData
        fields = [
            'title',
            'content',
            'author' 
        ]