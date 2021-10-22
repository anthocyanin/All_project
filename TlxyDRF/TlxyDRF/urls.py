from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from case01 import views

router = routers.SimpleRouter()
router.register(r'student', views.StudentVS, base_name="stu")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
