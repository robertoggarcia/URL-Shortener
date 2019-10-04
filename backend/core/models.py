import datetime
from django.contrib.auth.models import User
from django.db import models
import pandas as pd
from core.utils.base62_hash import get_hash


class Url(models.Model):
    id = models.CharField(max_length=2000, primary_key=True, editable=False)
    url = models.CharField(null=False, blank=False, max_length=200)
    short_url = models.CharField(null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.id = get_hash()
        self.short_url = self.id
        self.expire_at = datetime.datetime.now() + pd.DateOffset(years=2)
        super(Url, self).save(*args, **kwargs)
