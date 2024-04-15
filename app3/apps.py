from django.apps import AppConfig


class App3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app3'
    default = False

    def ready(self):
        pass

# waht is use of ready method here. test