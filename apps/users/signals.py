from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import Group

from .models import User, Librarian


@receiver(post_save, sender=User)
def give_librarian_user_staff_role(sender, **kwargs):

    if kwargs['created'] and kwargs['instance'].is_librarian():
        kwargs['instance'].is_staff = True
        Librarian.objects.create(user=kwargs['instance'])
        librarian_group = Group.objects.get(name='Librarian')
        librarian_group.user_set.add(kwargs['instance'])
        kwargs['instance'].save()
