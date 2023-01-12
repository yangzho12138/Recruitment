from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "jobs" # consist with the app name

    def ready(self):
        from jobs.signal_processor import post_save_callback, post_delete_callback
