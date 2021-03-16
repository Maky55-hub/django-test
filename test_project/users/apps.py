from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # when using signals, import needs to be done
    def ready(self):
        import users.signals
