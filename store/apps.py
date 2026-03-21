#from django.apps import AppConfig


#class StoreConfig(AppConfig):
#    name = 'store'

from django.apps import AppConfig
from django.contrib.auth import get_user_model

class MyAppConfig(AppConfig):
    name = 'store'

    def ready(self):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "", "%%&%%Beki123")
