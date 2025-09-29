from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import CustomUser
from accounts.utils.authtoken_utils import delete_user_tokens


@receiver(post_save, sender=CustomUser, weak=False)
def post_save_customuser(sender, instance, created, **kwargs):
    if not instance.is_active:
        delete_user_tokens(instance)
