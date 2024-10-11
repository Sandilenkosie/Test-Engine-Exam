from django.contrib import admin
from .models import Exam, Question, Answer,ExamResult,Group

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_filter = ('exam__title',)

class ExamAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Display fields in list view
    search_fields = ('title',)
    list_filter = ('group',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ExamResult)
admin.site.register(Group, GroupAdmin)
