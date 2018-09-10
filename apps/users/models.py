from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices


# Create your models here.
LIBRARIAN = 1
VISITOR = 2
STUDENT = 3

PROFILES = Choices(
    (LIBRARIAN, 'Librarian'),
    (VISITOR, 'Visitor'),
    (STUDENT, 'Student'),
)


class User(AbstractUser):
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    profile = models.IntegerField(choices=PROFILES, default=VISITOR)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    # Custom user methods
    def is_librarian(self):
        return True if self.profile == LIBRARIAN else False

    def is_visitor(self):
        return True if self.profile == VISITOR else False

    def is_student(self):
        return True if self.profile == STUDENT else False
