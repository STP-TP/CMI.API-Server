from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import usertbl
from CMI_Define.sql_define import *


# Create your views here.
def index(players):
    # 분석 안내 페이지 api의 양식을 정해야 한다
    test = {
        'nickname': 'blur',
        'level': 55,
        'grade': 'gold',
    }
    return HttpResponse(test)


def find_nickname(request, nickname):
    query_response = usertbl.objects.filter(**{NICKNAME: nickname})

    if query_response.exists() is False:
        return HttpResponse('404err')

    json_res = query_response.values()[0]
    del(json_res['id'])

    return JsonResponse(json_res, charset='utf-8')
    # return HttpResponse(tab.values())
