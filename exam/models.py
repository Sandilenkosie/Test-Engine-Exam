from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
import random
from django.core.files.base import ContentFile
from PIL import Image as PilImage
from io import BytesIO
import os

class Exam(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='exam_images/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='exam_thumbnails/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image:
            # Generate thumbnail
            image = PilImage.open(self.image)
            image.thumbnail((100, 100))  # Thumbnail size
            thumb_io = BytesIO()
            image.save(thumb_io, format='JPEG')
            thumb_file = ContentFile(thumb_io.getvalue(), name=os.path.basename(self.image.name))
            self.thumbnail.save(f'thumbnail_{self.image.name}', thumb_file, save=False)
        
        super().save(*args, **kwargs)

    def image_tag(self):
        if self.image:
            # If an image exists, display it
            return mark_safe(f'<img src="{self.image.url}" style="width: 50px; height: auto;" />')
        else:
            # Display a default placeholder image or text
            return mark_safe('<img src="https://readymadeui.com/cardImg.webp" />')
    
    image_tag.short_description = 'Image Preview'

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
