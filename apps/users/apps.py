from django.apps import AppConfig

# from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """

        from . import signals # noqa
