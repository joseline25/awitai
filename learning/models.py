from django.db import models
from student.models import Student

# Create your models here.


class StudentProfile(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="profile")  # one to one ????
    learning_style = models.CharField(max_length=1000)
    strong_points = models.TextField(blank=True, null=True)
    weaknesses = models.TextField(blank=True, null=True)
    interrests = models.TextField(blank=True, null=True)
    objectives = models.TextField()


class Game(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    points = models.IntegerField()
    success_criteria = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Badge(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    obtention_criteria = models.TextField()

    def __str__(self):
        return f"{self.name}"


class LearningLevel(models.Model):
    name = models.CharField(max_length=1000)
    required_experience = models.TextField()
    advantages = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Conversation(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="conversation")
    date = models.DateField()
    student_input = models.TextField()
    chatbot_answer = models.TextField()

    def __str__(self):
        return f"{self.student.first_name} - {self.date}"
