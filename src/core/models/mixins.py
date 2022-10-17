from __future__ import unicode_literals

import uuid as uuid_

from django.contrib.postgres import fields
from django.db import models
from django.utils.translation import gettext as _


class DateTimeMixin(models.Model):
    """
    This is model mixin with datetime info fields.
    """

    created_at = models.DateTimeField(  # type: ignore
        _("created at"),
        auto_now_add=True,
        auto_now=False,
        db_index=True,
        editable=False,
    )
    updated_at = models.DateTimeField(_("updated at"), auto_now_add=False, auto_now=True)  # type: ignore

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    """
    This is model mixin with uuid field.
    """

    uuid = models.UUIDField(  # type: ignore
        _("uuid"),
        default=uuid_.uuid4,
        unique=True,
        db_index=True,
        editable=False,
        help_text=_("Unique identifier"),
    )

    class Meta:
        abstract = True


class JsonMixin(models.Model):
    """
    This is model mixin with json field.
    """

    meta_data = fields.JSONField(  # type: ignore
        _("meta data"),
        editable=True,
        blank=True,
        null=True,
        default=None,
        help_text=_("Dynamic json field for additional data"),
    )

    class Meta:
        abstract = True
