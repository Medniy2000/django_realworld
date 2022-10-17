# Generated by Django 4.1 on 2022-10-17 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExampleModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique identifier",
                        unique=True,
                        verbose_name="uuid",
                    ),
                ),
                ("example_field", models.CharField(default=None, max_length=12)),
            ],
            options={
                "verbose_name": "example_model",
                "verbose_name_plural": "example_models",
                "db_table": "core_example_models",
            },
        ),
    ]