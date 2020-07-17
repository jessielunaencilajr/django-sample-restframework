from django.test import TestCase
from .models import School, Student, restrict_num_of_student
from django.core.exceptions import ValidationError
from faker import Faker
from model_mommy import mommy
# Create your tests here.

class UnitTestCase(TestCase):
    def test_school_str(self):
        school = mommy.make(School)
        self.assertTrue(isinstance(school, School))
        self.assertEqual(str(school), school.name)

    def test_school_zero_max(self):
        faker = Faker()
        school = School()
        school.name = faker.name()
        school.max_num_of_students = 0
        with self.assertRaises(ValidationError):
            school.full_clean()

    def test_restrict_num_of_student(self):
        faker = Faker()
        school = School()
        school.name = faker.name()
        school.max_num_of_students = 1
        school.save()
        with self.assertRaises(ValidationError):
            for x in range(1):
                student = Student()
                student.first_name = faker.name()[:19]
                student.last_name = faker.name()[:19]
                student.school = school
                student.save()
            restrict_num_of_student(school)

    def test_student_str(self):
        student = mommy.make(Student)
        self.assertTrue(isinstance(student, Student))
        self.assertEqual(str(student), f'{student.first_name} {student.last_name}')



