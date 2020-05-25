from __future__ import annotations

from typing import TYPE_CHECKING, Union

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

if TYPE_CHECKING:
    from polemicflow.users.models import User


class AuthoredModel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("author"),
    )

    class Meta:
        abstract = True

    def get_author(self) -> Union[User, AnonymousUser]:
        return self.author or AnonymousUser()


class CreatedFieldModel(models.Model):
    created = models.DateTimeField(_("created"), auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UpdatedFieldModel(models.Model):
    updated = models.DateTimeField(_("updated"), auto_now=True, editable=False)

    class Meta:
        abstract = True


class TimestampedModel(CreatedFieldModel, UpdatedFieldModel):
    class Meta:
        abstract = True
