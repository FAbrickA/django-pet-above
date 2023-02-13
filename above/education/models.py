from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=128, unique=True, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    subject = models.CharField(max_length=128)
    message = models.TextField(max_length=1024)

    created_dt = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return f"From: {self.name} | Subject: {self.subject}"
