from django.contrib import admin
from services.apps.credential_storage import models
from django.db.models.base import ModelBase

for model_name in dir(models):
    m = getattr(models, model_name)
    if isinstance(m, ModelBase) and not m._meta.abstract:
        try:
            admin.site.register(m)
        except admin.sites.AlreadyRegistered:
            pass
