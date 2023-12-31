# Generated by Django 4.2.1 on 2023-11-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mapsharing", "0002_playlist_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="geocodepoint",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="geocodepoint",
            name="point_name",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
    ]
