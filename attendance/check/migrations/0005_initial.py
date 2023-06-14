# Generated by Django 4.1.7 on 2023-05-09 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("check", "0004_delete_account_remove_course_students_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="student_info",
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
                ("major", models.CharField(max_length=20)),
                ("student_id", models.CharField(max_length=11)),
                (
                    "user_id",
                    models.OneToOneField(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]