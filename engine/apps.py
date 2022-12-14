from django.apps import AppConfig

#this is a base class
class EngineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engine'
