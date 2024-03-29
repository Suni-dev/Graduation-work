# Generated by Django 4.1.7 on 2023-06-05 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("check", "0018_user31337_usergroup31337_proinfo31337_stuinfo31337"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccAtt801",
            fields=[
                (
                    "stu",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="check.userelite",
                    ),
                ),
                (
                    "number_1week",
                    models.CharField(
                        blank=True, db_column="1week", max_length=50, null=True
                    ),
                ),
                (
                    "number_2week",
                    models.CharField(
                        blank=True, db_column="2week", max_length=50, null=True
                    ),
                ),
                (
                    "number_3week",
                    models.CharField(
                        blank=True, db_column="3week", max_length=50, null=True
                    ),
                ),
                (
                    "number_4week",
                    models.CharField(
                        blank=True, db_column="4week", max_length=50, null=True
                    ),
                ),
                (
                    "number_5week",
                    models.CharField(
                        blank=True, db_column="5week", max_length=50, null=True
                    ),
                ),
                (
                    "number_6week",
                    models.CharField(
                        blank=True, db_column="6week", max_length=50, null=True
                    ),
                ),
                (
                    "number_7week",
                    models.CharField(
                        blank=True, db_column="7week", max_length=50, null=True
                    ),
                ),
                (
                    "number_8week",
                    models.CharField(
                        blank=True, db_column="8week", max_length=50, null=True
                    ),
                ),
                (
                    "number_9week",
                    models.CharField(
                        blank=True, db_column="9week", max_length=50, null=True
                    ),
                ),
                (
                    "number_10week",
                    models.CharField(
                        blank=True, db_column="10week", max_length=50, null=True
                    ),
                ),
                (
                    "number_11week",
                    models.CharField(
                        blank=True, db_column="11week", max_length=50, null=True
                    ),
                ),
                (
                    "number_12week",
                    models.CharField(
                        blank=True, db_column="12week", max_length=50, null=True
                    ),
                ),
                (
                    "number_13week",
                    models.CharField(
                        blank=True, db_column="13week", max_length=50, null=True
                    ),
                ),
                (
                    "number_14week",
                    models.CharField(
                        blank=True, db_column="14week", max_length=50, null=True
                    ),
                ),
                (
                    "number_15week",
                    models.CharField(
                        blank=True, db_column="15week", max_length=50, null=True
                    ),
                ),
                ("acc_att_score", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "acc_att_801",
                "managed": False,
            },
        ),
    ]
