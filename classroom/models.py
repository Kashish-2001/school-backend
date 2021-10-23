from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    admission_number = models.PositiveIntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.first_name + str(self.admission_number)

    def get_grade(self):
        if 0 <= self.average_score < 40:
            return "Fail"
        elif 40 <= self.average_score < 75:
            return "Pass"
        elif 80 <= self.average_score <= 100:
            return "Excellent"
        else:
            return "Error"



class Classroom(models.Model):
    name = models.CharField(max_length=200)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
