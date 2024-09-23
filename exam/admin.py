from django.contrib import admin
from .models import Exam, Question, Answer,ExamResult

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ('exam__title',)

admin.site.register(Exam)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ExamResult)
