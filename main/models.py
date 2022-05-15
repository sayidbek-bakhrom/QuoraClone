from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify


class Question(models.Model):
    STATUS = (
        ('n', 'Named'),
        ('a', 'Anonymous'),
    )
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    slug = models.SlugField(unique=True, null=False)
    status = models.CharField(max_length=1, choices=STATUS, default='n')
    created_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('respond-question', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug == slugify(self.title)
        return super().save(*args, **kwargs)


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.body[:20]}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.user
