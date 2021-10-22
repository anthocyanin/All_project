from django.contrib import admin
from aadmin.models import Student, ClassRoom, Teacher
# Register your models here.
# 创建了一个超级管理员 用户名：lishangyin， 密码：qwe123
admin.site.site_header = "云月湖海"
admin.site.site_title = "我最棒"
admin.site.index_title = "if you unhappy--just fuck"


class ClassRoomAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ["name", "room", "cur_time", "get_room_name"]
    search_fields = ["name"]
    # fields = ["name", "course"] fields 和 fieldsets只能同时设置一个
    fieldsets = (
        ("基本信息", {"fields": ["name", ]}),
        ("其他信息", {"fields": ["room", "course"]}),
    )


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)

