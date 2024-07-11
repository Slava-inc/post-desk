from django.apps import AppConfig


class DeskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'desk'

    def ready(self) -> None:
        import Post_desk.article.signals