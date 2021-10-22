from django.contrib import admin
from admin_manage.models import Student, ClassRoom, Teacher
# Register your models here.
admin.site.site_header = "欢迎来django课程"
admin.site.site_title = "北京图灵学院欢迎你"
admin.site.index_title = "图灵学院欢天下第一"


class ClassRoomAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ["name", "room", "curTime","getRoomName"]
    search_fields = ["name"]
    # fields = ["name", "course"]
    fieldsets = (
        ("基本信息", {"fields":["name"]}),
        ("其他信息", {"fields":["room", "course"]}),

    )


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)


