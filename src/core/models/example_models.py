from django.db import models
from django.utils.translation import gettext as _
from src.core.models import mixins as db_mixins


class ExampleModel(db_mixins.UUIDMixin, db_mixins.DateTimeMixin, models.Model):
    example_field = models.CharField(default=None, max_length=12)  # type: ignore

    class Meta:
        db_table = "core_example_models"
        verbose_name = _("example_model")
        verbose_name_plural = _("example_models")
