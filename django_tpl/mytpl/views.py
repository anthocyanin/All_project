from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def one(request):
    return render(request, r"one.html")


def two(request):
    ct = dict()
    ct["name"] = "wangxiaojing"
    ct["name2"] = "liuxiaojing"
    ct["name3"] = "xuxiaojing"
    return render(request, r"two.html", context=ct)


def three(request):
    ct = dict()
    ct["score"] = [99, 98, 100, 25, 56, 78]
    return render(request, r"three.html", context=ct)


def four(request):
    ct = dict()
    ct["name"] = "王晓静"

    return render(request, r"four.html", context=ct)


def five_get(request):
    return render(request, "five_get.html")


def five_post(request):
    print(request.POST)
    return render(request, "one.html")






