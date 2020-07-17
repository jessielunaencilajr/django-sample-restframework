from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator 

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=20)
    max_num_of_students = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

def restrict_num_of_student(school):
    if Student.objects.filter(school=school).count() >= school.max_num_of_students:
        raise ValidationError(f'Cannot exceed {school} max number of student of {school.max_num_of_students}')

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE, validators=(restrict_num_of_student, ))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.id:
            import random
            self.student_id = str(random.randint(1,999999))

        super(Student, self).save(*args, **kwargs)