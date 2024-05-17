# Generated by Django 5.0.6 on 2024-05-17 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Reading', 'Reading'), ('Writing', 'Writing'), ('Mathematics', 'Mathematics'), ('Critical Thinking', 'Critical Thinking')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('starter', 'starter'), ('intermediary', 'intermediary'), ('advanced', 'advanced')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Progression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=1000)),
                ('membership_fee', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('region', models.CharField(blank=True, choices=[('Center', 'Center'), ('Littoral', 'Littoral'), ('South', 'South'), ('West', 'West'), ('North', 'North'), ('Far North', 'Far North'), ('Adamawa', 'Adamawa'), ('North West', 'North West'), ('East', 'East'), ('South West', 'South West')], max_length=1000, null=True)),
                ('level', models.CharField(blank=True, choices=[('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B')], max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('region', models.CharField(blank=True, choices=[('Center', 'Center'), ('Littoral', 'Littoral'), ('South', 'South'), ('West', 'West'), ('North', 'North'), ('Far North', 'Far North'), ('Adamawa', 'Adamawa'), ('North West', 'North West'), ('East', 'East'), ('South West', 'South West')], max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('Reading', 'Reading'), ('Writing', 'Writing'), ('Mathematics', 'Mathematics'), ('Critical Thinking', 'Critical Thinking')], max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('type_of_competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='student.competency')),
                ('level_of_difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_level', to='student.level')),
            ],
        ),
        migrations.CreateModel(
            name='HasCompetency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.TextField()),
                ('notes', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.activity')),
                ('competency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.competency')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.level')),
                ('progression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='student.progression')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('evaluator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='competency',
            name='student',
            field=models.ManyToManyField(related_name='competencies', through='student.HasCompetency', to='student.student'),
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(blank=True, max_length=1000, null=True)),
                ('link', models.URLField()),
                ('teacher', models.ManyToManyField(related_name='ressources', to='student.teacher')),
            ],
        ),
    ]