# Generated by Django 4.1 on 2022-10-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_createdinstrument_error_message_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("group_number", models.IntegerField(unique=True)),
                ("group_name", models.CharField(max_length=255, unique=True)),
                ("missing", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["group_number"],
            },
        ),
        migrations.AlterModelOptions(
            name="study",
            options={"ordering": ["study_number"], "verbose_name_plural": "studies"},
        ),
        migrations.RemoveField(
            model_name="instrument",
            name="orig_study_field_name",
        ),
        migrations.RemoveField(
            model_name="instrument",
            name="studies_field_name",
        ),
        migrations.AddField(
            model_name="instrument",
            name="instrument_label",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="study",
            name="missing",
            field=models.BooleanField(default=False),
        ),
    ]
