from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(get_user_model(), related_name="tags", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.name}"


class Note(models.Model):
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="notes")
    author = models.ForeignKey(get_user_model(), related_name="notes", on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.author.username}: {self.text[:20] if not self.deleted else '<deleted>'}"
