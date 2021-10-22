from django.conf.urls import include, url
from django.contrib import admin
# from sess import views as v


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^sess/', v.my_sess),
    # url(r'^stu/', v.StudentListView.as_view()),
]
