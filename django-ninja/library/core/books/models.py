from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django_extensions.db.fields import AutoSlugField


class User(AbstractUser):
    pass


class Author(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    birthdate = models.DateField()


    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=13)
    pub_date = models.DateField()
    slug = AutoSlugField(populate_from="title", unique=True)
    is_deleted = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    class Meta:
        ordering = ["-pub_date"]

