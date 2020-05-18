from django.urls import path
from Analysis import views

urlpatterns = [
    # /Analysis1/
    path('', views.index, name='index'),
]
