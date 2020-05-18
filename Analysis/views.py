from django.http import HttpResponse
from django.contrib.auth.models import User, Group
# from .models import Analysis


# Create your views here.
def index(player):
    test = {
        'nickname': 'blur',
        'level': 55,
        'grade': 'gold',
    }
    return HttpResponse(test)
