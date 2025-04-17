from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import random

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='exam_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return "https://ui-avatars.com/api/?name=Blue+Ghost"

    def image_tag(self):
        return mark_safe(f'<img src="{self.get_image_url()}" style="width: auto; height: auto;" />')

    image_tag.short_description = 'Image Preview'

    def __str__(self):
        return self.name



class Exam(models.Model):
    title = models.CharField(max_length=255)
    group = models.ManyToManyField(Group, related_name='exams', blank=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    multiple_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    @staticmethod
    def get_shuffled_questions(exam):
        questions = list(Question.objects.filter(exam=exam))
        random.shuffle(questions)
        return questions

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
    @staticmethod
    def get_shuffled_answers(question):
        answers = list(Answer.objects.filter(question=question))   
        random.shuffle(answers)
        return answers

class ExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    percentage_score = models.FloatField()
    correct_answers = models.JSONField()  # Store answers as JSON
    wrong_answers = models.JSONField()  # Store answers as JSON
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.exam}"

class ExamResultOption(models.Model):
    exam_result = models.ForeignKey(ExamResult, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)

    class Meta:
        unique_together = ('exam_result', 'answer')
