from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Question(models.Model):
    STATUS = (
        ('n', 'Named'),
        ('a', 'Anonymous'),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='n')
    created_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.body[:10]}'

