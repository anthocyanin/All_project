from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.


def do_normalmap(request):
    return HttpResponse("this is normalmap")


def withparam(request, year, month):
    return HttpResponse("this is with param {0}, {1}".format(year, month))


def do_app(r):
    return HttpResponse("这是一个子路由")


def do_param2(r, pn):
    return HttpResponse("page number is {0}".format(pn))


def extreParam(r, name):
    return HttpResponse("my name is {0}".format(name))


def revParse(r):
    return HttpResponse("your requested url is {0}".format(reverse("askname")))

