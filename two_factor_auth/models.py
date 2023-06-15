from django.db import models
from django.conf import settings

from random import choice
from string import digits

class TwoFactorAuthModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)

    def __str__(self):
        return self.user.username 
    
    def save(self, *args, **kwargs):
        self.token = ''.join(choice(digits) for _ in range(6))
        super().save(*args, **kwargs)
