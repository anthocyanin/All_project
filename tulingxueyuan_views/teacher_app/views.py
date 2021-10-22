from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.


def teacher(r):
    return HttpResponse("这是一个teacher下的视图")


def v2_exception(r):
    raise Http404
    return HttpResponse("ok")


def v10_1(r):
    return HttpResponseRedirect("/v11")


def v10_2(r):
    return HttpResponseRedirect(reverse("v11"))


def v11(r):
    return HttpResponse("哈哈 这是v11的访问返回")


def v8_get(request):
    rst = ""
    for k, v in request.GET.items():
        rst += k + "-->" + v
        rst += ","

    return HttpResponse("get value of Request is {}".format(rst))


def v9_get(request):
    return render_to_response("for_post.html")


def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("get value of POST is {0}".format(rst))


def render_test(request):
    # 环境变量
    # C = dict()
    rsp = render(request, "render.html")

    return rsp


def render2_test(request):

    c = dict()
    c["name"] = "liudana"
    c["name2"] = "liukana"
    c["name3"] = "liumana"

    rsp = render(request, "render2.html", context=c)

    return rsp


def render3_test(request):
    from django.template import loader
    # 得到模板
    t = loader.get_template("render2.html")
    print(type(t))

    rsp = t.render({"name": "liuGana"})
    print(type(rsp))

    return HttpResponse(rsp)


def render4_test(request):

    rsp = render_to_response("render2.html", context={"name":"liudaza"})
    return rsp


def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request, Exception)













