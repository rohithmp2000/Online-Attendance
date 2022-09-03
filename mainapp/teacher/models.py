from django.db import models
from core.models import UserRole

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    roletype = models.OneToOneField(UserRole, on_delete=models.CASCADE, related_name='teacher')
    SUBJECT_CHOICES = (
        ("1", "Computer Science"),
        ("2", "Physics"),
        ("3", "Chemistry"),
        ("4", "Biology"),
        ("5", "Maths"),
        ("6", "English"),
    )
    subject = models.CharField(choices=SUBJECT_CHOICES,max_length=1,blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name