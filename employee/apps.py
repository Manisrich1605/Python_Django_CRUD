from django.apps import AppConfig


class EmployeeConfig(AppConfig):#application config inherit appconfig
    default_auto_field = 'django.db.models.BigAutoField'#default primarykey for models------bigint primary key field
    name = 'employee'#app name
