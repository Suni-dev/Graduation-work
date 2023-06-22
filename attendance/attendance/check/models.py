# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(models.Manager):
    def create_user(self, id, password=None, **extra_fields):
        user = self.model(id=id, **extra_fields)
        if password:
            user.password = make_password(password)
        user.save()
        return user

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=125, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    usermajor = models.CharField(max_length=50, blank=True, null=True)
    usergroup = models.ForeignKey('UserGroup', models.DO_NOTHING, db_column='usergroup', blank=True, null=True)

    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'user'


class UserGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'


class Class(models.Model):
    subject = models.CharField(unique=True, max_length=50, blank=True, null=True)
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    day_of_week = models.CharField(max_length=3, blank=True, null=True)
    class_time = models.CharField(max_length=1, blank=True, null=True)
    class_room = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Attendance80131337(models.Model):
    student_id = models.CharField(max_length=50, blank=True, null=True)
    student_name = models.CharField(max_length=50, blank=True, null=True)
    attendance_status = models.CharField(max_length=50, blank=True, null=True)
    class_time = models.CharField(max_length=50, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    late_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_801_31337'


class Attendance801Elite(models.Model):
    student_id = models.CharField(max_length=50, blank=True, null=True)
    student_name = models.CharField(max_length=50, blank=True, null=True)
    attendance_status = models.CharField(max_length=50, blank=True, null=True)
    class_time = models.CharField(max_length=50, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    late_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_801_elite'


class AccAtt801(models.Model):
    stu = models.OneToOneField(User, models.DO_NOTHING, primary_key=True,to_field='id')
    subject = models.ForeignKey(Class, models.DO_NOTHING, to_field='subject', blank=True, null=True)
    number_1week = models.CharField(db_column='1week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2week = models.CharField(db_column='2week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3week = models.CharField(db_column='3week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4week = models.CharField(db_column='4week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5week = models.CharField(db_column='5week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6week = models.CharField(db_column='6week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_7week = models.CharField(db_column='7week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_8week = models.CharField(db_column='8week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_9week = models.CharField(db_column='9week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_10week = models.CharField(db_column='10week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_11week = models.CharField(db_column='11week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_12week = models.CharField(db_column='12week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_13week = models.CharField(db_column='13week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_14week = models.CharField(db_column='14week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_15week = models.CharField(db_column='15week', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    acc_att_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_att_801'

    def calculate_attendance_score(self):
        week_fields = [
            'number_1week', 'number_2week', 'number_3week', 'number_4week',
            'number_5week', 'number_6week', 'number_7week', 'number_8week',
            'number_9week', 'number_10week', 'number_11week', 'number_12week',
            'number_13week', 'number_14week', 'number_15week'
        ]
        attendance_values = {
            '출석': 1,
            '지각': 0.5,
            '결석': 0
        }
        score = 0
        for field in week_fields:
            value = getattr(self, field)
            if value in attendance_values:
                score += attendance_values[value]
        return score

    def save(self, *args, **kwargs):
        self.acc_att_score = self.calculate_attendance_score()
<<<<<<< HEAD
        super().save(*args, **kwargs)
=======
        super().save(*args, **kwargs)
>>>>>>> f9f3843 (최종수정)
