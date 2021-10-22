from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from Myser import views

# router = routers.SimpleRouter()
# router.register(r'student', views.StudentVS, base_name='stu')
# router.register(r'apiview', views.StudentAPIView, base_name='apiview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/apiview', views.StudentAPIView.as_view()),
    path('api/apigenview', views.StudentGenAPIView.as_view())
]
