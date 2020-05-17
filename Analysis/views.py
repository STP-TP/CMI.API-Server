from django.http import HttpResponse
from django.contrib.auth.models import User, Group
# from .models import Analysis
from Analysis.serializers import AnalysisSerializer
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.
def index(player):
    test = {
        'nickname': 'blur',
        'level': 55,
        'grade': 'gold',
    }
    return HttpResponse(test)


class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = AnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]
