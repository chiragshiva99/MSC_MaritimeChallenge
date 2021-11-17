from django.contrib import admin
from .models import *


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

# class AnswerInline4(admin.TabularInline):
#     model = Answer4

# class QuestionAdmin4(admin.ModelAdmin):
#     inlines = [AnswerInline4]

# admin.site.register(Question4, QuestionAdmin4)
# admin.site.register(Answer4)