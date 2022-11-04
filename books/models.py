from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'books'