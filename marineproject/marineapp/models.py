from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.enums import Choices
from django.forms.fields import CharField
from multiselectfield import MultiSelectField
from django.forms import ModelForm

# Create your models here.


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("Full Name", max_length=250)
    email = models.EmailField()
    hr = models.BooleanField("HR", default=False)
    trainer = models.BooleanField("Trainer", default=False)
    trainee = models.BooleanField("Trainee", default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'User- HR, Trainee, Trainer'


class LessonMaterialModule1(models.Model):
    topic = models.CharField(max_length=1000)
    pdf_file = models.FileField(upload_to='lesson_module1')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Module 1 Lesson'


class LessonMaterialModule2(models.Model):
    topic = models.CharField(max_length=1000)
    pdf_file = models.FileField(upload_to='lesson_module2')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Module 2 Lesson'


class LessonMaterialModule3(models.Model):
    topic = models.CharField(max_length=1000)
    pdf_file = models.FileField(upload_to='lesson_module3')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Module 3 Lesson'


class LessonMaterialModule4(models.Model):
    topic = models.CharField(max_length=1000)
    pdf_file = models.FileField(upload_to='lesson_module4')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Module 4 Lesson'


class LessonMaterialModule5(models.Model):
    topic = models.CharField(max_length=1000)
    pdf_file = models.FileField(upload_to='lesson_module5')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Module 5 Lesson'


# class Answer(models.Model):
#     question_relation = models.ForeignKey(Hangman, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.answer