from rest_framework import serializers
from api.models import Keyword_List

class Keyword_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword_List
        fields = ('text', 'category')