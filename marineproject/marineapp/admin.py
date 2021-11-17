from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(
    [Customer, LessonMaterialModule1, LessonMaterialModule2, LessonMaterialModule3, LessonMaterialModule4, LessonMaterialModule5])
