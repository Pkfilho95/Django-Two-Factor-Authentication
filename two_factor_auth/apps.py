from django.apps import AppConfig

class TwoFactorAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'two_factor_auth'

    def ready(self):
        import two_factor_auth.signals
