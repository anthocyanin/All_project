from rest_framework import serializers
from Myser.models import Student


class StudentSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(label="姓名", max_length=20)
    # age = serializers.IntegerField()
    # score = serializers.IntegerField()
    class Meta:
        model = Student
        fields = '__all__'

