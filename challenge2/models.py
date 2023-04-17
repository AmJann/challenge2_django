from django.db import models
from django.contrib.auth.models import User
import uuid

class ToDo(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    title = models.Column(Charfield(max_length=50))
    description = models.Column(Charfield(max_length=500))
    date_due = models.Column(DateField())
    in_progress = models.Column(BooleanField(default=False))
    complete = models.Column(BooleanField(default=False))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.user} | {self.title}"