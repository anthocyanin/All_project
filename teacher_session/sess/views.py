from django.shortcuts import render
# from django.core.paginator import Paginator
# from django.views.generic import ListView
# from sess.models import *
#
#
# class StudentListView(ListView):
#     queryset = Student.objects.all().filter(gender="man")
#     template_name = "student_list.html"
#
#
# def my_sess(request):
#     print(type(request.session))
#     print(request.session)
#     print(request.session.get("teacher_name", "no name"))
#     request.session.clear()
#     print("my session")
#     return None
#
#
# def student(request):
#     stus = Student.objects.all()
#     p = Paginator(stus, 50)
#     print(p.count)  # 页面总数据
#     print(p.num_pages)  # 页面总数
#     print(p.page_range)  # 页码列表
#     print(p.page(3))
#     return stus



