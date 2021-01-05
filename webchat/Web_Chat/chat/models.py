from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Messages(models.Model):
    msg_from=models.ForeignKey(User,on_delete=models.CASCADE, related_name='msg_from')
    msg_to=models.ForeignKey(User,on_delete=models.CASCADE, related_name='msg_to')
    msg_text=models.TextField()
    date_postdate=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.msg_text


