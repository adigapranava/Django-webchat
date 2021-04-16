from django.db import models
from django.contrib.auth.models import User
from chat.models import Messages

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', height_field=None)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def last_msg(self, pk1, pk2):
        # try:
            # Messages.objects.filter(msg_from = )