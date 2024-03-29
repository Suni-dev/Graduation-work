# Generated by Django 4.1.7 on 2023-05-08 16:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("check", "0003_alter_userprofile_user"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Account",
        ),
        migrations.RemoveField(
            model_name="course",
            name="students",
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="course",
        ),
        migrations.RemoveField(
            model_name="enrollment",
            name="student",
        ),
        migrations.RemoveField(
            model_name="student",
            name="user",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Attendance",
        ),
        migrations.DeleteModel(
            name="Course",
        ),
        migrations.DeleteModel(
            name="Enrollment",
        ),
        migrations.DeleteModel(
            name="Student",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
