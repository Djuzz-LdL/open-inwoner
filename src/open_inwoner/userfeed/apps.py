from django.apps import AppConfig


class UserFeedConfig(AppConfig):
    name = "open_inwoner.userfeed"
    label = "userfeed"
    verbose_name = "User Feed"

    def ready(self):
        auto_import_adapters()

        from .hooks.external_task import fetch_open_tasks  # noqa


def auto_import_adapters():
    """
    import files from hooks directory to register adapters
    """
    import open_inwoner.userfeed.hooks  # noqa
