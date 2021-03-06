from django.db import models

# Create your models here.
from nectr.tutor.models import Tutor
from nectr.users.models import User


class Student(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    ram_id = models.TextField(default='R00000000')
    votes = models.IntegerField(default=0)

class StudentLikes(Student):
    liked_tutors = models.ForeignKey(Tutor)
