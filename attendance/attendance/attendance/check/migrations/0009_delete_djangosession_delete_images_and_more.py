# Generated by Django 4.1.7 on 2023-05-12 01:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("check", "0008_attendance_delete_checkcustomuser_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DjangoSession",
        ),
        migrations.DeleteModel(
            name="Images",
        ),
        migrations.DeleteModel(
            name="ProfessorInfo",
        ),
        migrations.DeleteModel(
            name="Readme",
        ),
        migrations.DeleteModel(
            name="StudentInfo",
        ),
        migrations.AlterModelTable(
            name="attendance",
            table="attendance",
        ),
    ]
