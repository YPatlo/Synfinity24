# Generated by Django 5.1.1 on 2024-10-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "synfinity24",
            "0003_enigma_imaginarte_logolegends_resonance_tetrarealm_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="enigma",
            name="std2Class",
            field=models.TextField(default="null"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="enigma",
            name="std2Name",
            field=models.TextField(default="null"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="enigma",
            name="teamName",
            field=models.TextField(default="null"),
            preserve_default=False,
        ),
    ]
