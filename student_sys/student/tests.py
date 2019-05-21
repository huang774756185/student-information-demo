from django.test import TestCase
from .models import Student
# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
                name = "huanghuang123",
                sex = 1,
                email = "55@qq.com",
                profession = "东皇",
                qq = "445333543",
                phone = "244556",
         )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
                      name = "huanghuang123",
                      sex = 0,
                      email = "545@qq.com",
                      profession = "东皇",
                      qq = "445333543",
                      phone = "244556",

        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟显示不一致')

    def test_filter(self):
        student = Student.objects.create(
                       name = "huanghuang123",
                       sex = 1,
                       email = "545@qq.com",
                       profession = "东皇",
                       qq = "445333543",
                       phone = "244556",
        )  
        name = "huanghuang123"
        students = Student.objects.filter(name = name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))
