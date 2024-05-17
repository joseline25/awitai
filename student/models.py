from django.db import models


regions = [
    ('Center', 'Center'),
    ('Littoral', 'Littoral'),
    ('South', 'South'),
    ('West', 'West'),
    ('North', 'North'),
    ('Far North', 'Far North'),
    ('Adamawa', 'Adamawa'),
    ('North West', 'North West'),
    ('East', 'East'),
    ('South West', 'South West'),
]

levels = [
    ('A+', "A+"),
    ('A', "A"),
    ('B+', 'B+'),
    ('B', 'B'),
]

types = [
    ('Reading', "Reading"),
    ('Writing', "Writing"),
    ('Mathematics', 'Mathematics'),
    ('Critical Thinking', 'Critical Thinking'),
]

# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True, db_index=True)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    membership_fee = models.BooleanField(default=True)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    region = models.CharField(
        max_length=1000, choices=regions, blank=True, null=True)
    level = models.CharField(
        max_length=1000, choices=levels, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date joined")
    updated_at = models.DateTimeField(auto_now=True)


class Competency(models.Model):

    type = models.CharField(choices=types, max_length=1000)
    student = models.ManyToManyField(
        Student, related_name='competencies', through="HasCompetency")


class HasCompetency(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    competency = models.ForeignKey("Competency", on_delete=models.CASCADE)
    test_date = models.DateTimeField(auto_now_add=True)
    evaluator = models.ForeignKey(
        "Teacher", on_delete=models.CASCADE, blank=True, null=True)
    remarks = models.TextField()
    notes = models.TextField()
    level = models.ForeignKey(
        "Level", on_delete=models.CASCADE, blank=True, null=True)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)
    progression = models.ForeignKey(
        "Progression", on_delete=models.CASCADE, related_name="student")

    def __str__(self):
        return f"{self.activity}- {self.level} "


class Level(models.Model):

    levels = [
        ('starter', "starter"),
        ('intermediary', "intermediary"),
        ('advanced', 'advanced'),

    ]
    type = models.CharField(choices=levels, max_length=1000)

    def __str__(self):
        return f"{self.type}"


class Activity(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    level_of_difficulty = models.ForeignKey(
        Level, on_delete=models.CASCADE, related_name="activities_level")
    type_of_competence = models.ForeignKey(
        Competency, related_name="activities", on_delete=models.CASCADE)
    type_of_evaluation = models.ManyToManyField(Student, through="Evaluation")

    def __str__(self):
        return f"{self.title}- {self.level_of_difficulty}"


class Evaluation(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="evaluation")
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="evaluation")
    date = models.DateTimeField()
    score = models.IntegerField()
    comment = models.TextField()


class Progression(models.Model):
    date = models.DateTimeField()
    score = models.IntegerField()
    comment = models.TextField()


class Ressource(models.Model):
    document = models.CharField(max_length=1000, blank=True, null=True)
    link = models.URLField()
    teacher = models.ManyToManyField("Teacher", related_name="ressources")


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, db_index=True)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    region = models.CharField(
        max_length=1000, choices=regions, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date joined")
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=types, max_length=1000)

    def __str__(self):
        return f"{self.first_name}- {self.last_name}"
