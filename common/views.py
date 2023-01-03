from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("전체 사이트 인덱스입니다.")