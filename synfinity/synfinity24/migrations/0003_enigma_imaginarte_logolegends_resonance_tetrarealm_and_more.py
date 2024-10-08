# Generated by Django 5.1.1 on 2024-09-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "synfinity24",
            "0002_octave_accteacher_octave_std1class_octave_std1name_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Enigma",
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
                ("schoolName", models.TextField()),
                ("schoolEmail", models.TextField()),
                ("accTeacher", models.TextField()),
                ("std1Name", models.TextField()),
                ("std1Class", models.TextField()),
                ("teamEmail", models.TextField()),
                ("teacherEmail", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="ImaginArte",
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
                ("schoolName", models.TextField()),
                ("schoolEmail", models.TextField()),
                ("accTeacher", models.TextField()),
                ("teamName", models.TextField()),
                ("std1Name", models.TextField()),
                ("std2Name", models.TextField()),
                ("std1Class", models.TextField()),
                ("std2Class", models.TextField()),
                ("teamEmail", models.TextField()),
                ("teacherEmail", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="LogoLegends",
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
                ("schoolName", models.TextField()),
                ("schoolEmail", models.TextField()),
                ("accTeacher", models.TextField()),
                ("teamName", models.TextField()),
                ("std1Name", models.TextField()),
                ("std2Name", models.TextField()),
                ("std3Name", models.TextField()),
                ("std1Class", models.TextField()),
                ("std2Class", models.TextField()),
                ("std3Class", models.TextField()),
                ("teamEmail", models.TextField()),
                ("teacherEmail", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Resonance",
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
                ("schoolName", models.TextField()),
                ("schoolEmail", models.TextField()),
                ("accTeacher", models.TextField()),
                ("teamName", models.TextField()),
                ("std1Name", models.TextField()),
                ("std2Name", models.TextField()),
                ("std3Name", models.TextField()),
                ("std1Class", models.TextField()),
                ("std2Class", models.TextField()),
                ("std3Class", models.TextField()),
                ("teamEmail", models.TextField()),
                ("teacherEmail", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Tetrarealm",
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
                ("schoolName", models.TextField()),
                ("schoolEmail", models.TextField()),
                ("accTeacher", models.TextField()),
                ("teamName", models.TextField()),
                ("std1Name", models.TextField()),
                ("std2Name", models.TextField()),
                ("std3Name", models.TextField()),
                ("std1Class", models.TextField()),
                ("std2Class", models.TextField()),
                ("std3Class", models.TextField()),
                ("teamEmail", models.TextField()),
                ("teacherEmail", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="VortexVentures",
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
                ("schoolName", models.TextField()),
                ("schoolEmail", models.TextField()),
                ("accTeacher", models.TextField()),
                ("teamName", models.TextField()),
                ("std1Name", models.TextField()),
                ("std2Name", models.TextField()),
                ("std3Name", models.TextField()),
                ("std4Name", models.TextField()),
                ("std1Class", models.TextField()),
                ("std2Class", models.TextField()),
                ("std3Class", models.TextField()),
                ("std4Class", models.TextField()),
                ("teamEmail", models.TextField()),
                ("teacherEmail", models.TextField()),
            ],
        ),
    ]
