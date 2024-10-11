from django.contrib import admin
from .models import Exam, Question, Answer,ExamResult

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ('exam__title',)

class ExamAdmin(admin.ModelAdmin):
    list_display = ('image','title',)  # Display fields in list view
    search_fields = ('title',)


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ExamResult)
