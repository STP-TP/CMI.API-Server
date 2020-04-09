from .models import Analysis
from rest_framework import serializers, viewsets


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
