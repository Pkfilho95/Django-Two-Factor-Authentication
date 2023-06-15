from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TwoFactorAuthModel

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_generate_two_factor_auth(sender, instance, created, *args, **kwargs):
    if created:
        TwoFactorAuthModel.objects.create(
            user = instance
        )