from rest_framework import serializers
# from .models import Analysis
from django.contrib.auth.models import User, Group


class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
