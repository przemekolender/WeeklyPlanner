from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
from django.http import request


class UserData(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.username)


class Teams(models.Model):
    name = models.CharField(max_length=100, null=True)
    users = models.ManyToManyField(UserData)

    def __str__(self):
        return self.name


class Task(models.Model):
    statusCategory = (
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Done', 'Done'))

    priorityCategory = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Super important', 'Super Important')
    )

    title = models.CharField(max_length=120, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    priority = models.CharField(max_length=20, choices=priorityCategory, default=priorityCategory[1])
    status = models.CharField(max_length=20, choices=statusCategory, default=statusCategory[0])
    user = models.ForeignKey(UserData, null=True, on_delete=models.SET_NULL, blank=True)
    team = models.ForeignKey(Teams, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return str(self.title)


class Events(models.Model):
    name = models.CharField(max_length=120, null=True)
    desc = models.CharField(max_length=120, null=True, blank=True)
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True)
    user = models.ForeignKey(UserData, null=True, on_delete=models.SET_NULL, blank=True)
    team = models.ForeignKey(Teams, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.name
