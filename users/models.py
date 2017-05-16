from django.db import models
from custom_user.models import AbstractEmailUser
from django.utils.translation import ugettext as _
from helpers.models import BaseModel


class User(AbstractEmailUser, BaseModel):
    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
