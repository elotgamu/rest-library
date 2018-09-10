from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import User


@receiver(post_save, sender=User)
def give_librarian_user_staff_role(sender, **kwargs):

    if kwargs['created'] and kwargs['instance'].is_librarian():
        kwargs['instance'].is_staff = True
        kwargs['instance'].save()
