from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  image = models.CharField(max_length=300, blank=True)
  # analytical data
  created_at = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
  created_by = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'todo'
