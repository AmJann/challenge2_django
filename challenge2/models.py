from django.db import models
from users.models import User
import uuid

class ToDo(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_due = models.DateField()
    in_progress = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.title}"