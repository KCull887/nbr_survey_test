# Generated by Django 4.1 on 2023-12-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0013_instrumentcreationrule_strict_operator"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstrumentCreationEventLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("started", "started"),
                            ("finished", "finished"),
                            ("never_finished", "never_finished"),
                        ],
                        default="started",
                        max_length=20,
                    ),
                ),
                ("start", models.DateTimeField()),
                ("finish", models.DateTimeField(blank=True, null=True)),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
