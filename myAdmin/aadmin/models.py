from django.db import models
import time


class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

    def __str__(self):
        return self.roomName


class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)
    room = models.OneToOneField(ClassRoom, on_delete=models.CASCADE)

    def get_room_name(self):
        return self.room.roomName
    get_room_name.short_description = "教室"

    def cur_time(self):
        return time.time()
    cur_time.short_description = "当前时间"
    cur_time.admin_order_field = "name"

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




