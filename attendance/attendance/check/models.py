# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.hashers import make_password

class AccAtt801(models.Model):
    stu = models.OneToOneField('UserElite', models.DO_NOTHING, primary_key=True)
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
    acc_att_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_att_801'


class AccAttendanceElite(models.Model):
    stu_id = models.CharField(max_length=50, blank=True, null=True)
    stu_name = models.CharField(max_length=50, blank=True, null=True)
    att_score = models.IntegerField(blank=True, null=True)
    acc_att_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_attendance_elite'


class Attendance(models.Model):
    stu_id = models.CharField(max_length=50, blank=True, null=True)
    stu_name = models.CharField(max_length=50, blank=True, null=True)
    attendance_status = models.CharField(max_length=50, blank=True, null=True)
    attendance_score = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance'


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
    class_time = models.CharField(max_length=50, blank=True, null=True)
    attendance_status = models.CharField(max_length=50, blank=True, null=True)
    late_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_801_elite'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Class(models.Model):
    subject = models.CharField(max_length=50, blank=True, null=True)
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    day_of_week = models.CharField(max_length=3, blank=True, null=True)
    class_time = models.CharField(max_length=1, blank=True, null=True)
    class_room = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Images(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class ProInfo31337(models.Model):
    pro = models.OneToOneField('User31337', models.DO_NOTHING, primary_key=True, related_name='proinfo31337_pro')
    pro_name = models.CharField(max_length=50, blank=True, null=True)
    pro_major = models.CharField(max_length=50, blank=True, null=True)
    group = models.ForeignKey('UserGroup31337', models.DO_NOTHING, db_column='group', blank=True, null=True, related_name='proinfo31337_group')

    class Meta:
        managed = False
        db_table = 'pro_info_31337'


class ProInfoElite(models.Model):
    pro = models.OneToOneField('UserElite', models.DO_NOTHING, primary_key=True, related_name='proinfoelite_pro')
    pro_name = models.CharField(max_length=50, blank=True, null=True)
    pro_major = models.CharField(max_length=50, blank=True, null=True)
    group = models.ForeignKey('UserGroupElite', models.DO_NOTHING, db_column='group', blank=True, null=True, related_name='proinfoelite_group')

    class Meta:
        managed = False
        db_table = 'pro_info_elite'


class StuInfo31337(models.Model):
    stu = models.OneToOneField('User31337', models.DO_NOTHING, primary_key=True, related_name='stuinfo31337_stu')
    stu_name = models.CharField(max_length=50, blank=True, null=True)
    stu_major = models.CharField(max_length=50, blank=True, null=True)
    group = models.ForeignKey('UserGroup31337', models.DO_NOTHING, db_column='group', blank=True, null=True, related_name='stuinfo31337_group')

    class Meta:
        managed = False
        db_table = 'stu_info_31337'


class StuInfoElite(models.Model):
    stu = models.OneToOneField('UserElite', models.DO_NOTHING, primary_key=True, related_name='stuinfoelite_stu')
    stu_name = models.CharField(max_length=50, blank=True, null=True)
    stu_major = models.CharField(max_length=50, blank=True, null=True)
    group = models.ForeignKey('UserGroupElite', models.DO_NOTHING, db_column='group', blank=True, null=True, related_name='stuinfoelite_group')

    class Meta:
        managed = False
        db_table = 'stu_info_elite'


class User31337Manager(models.Manager):
    def create_user(self, id, password=None, **extra_fields):
        user = self.model(id=id, **extra_fields)
        if password:
            user.password = make_password(password)
        user.save()
        return user

class User31337(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=125, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    usermajor = models.CharField(max_length=50, blank=True, null=True)
    usergroup = models.ForeignKey('UserGroup31337', models.DO_NOTHING, db_column='usergroup', blank=True, null=True, related_name='user31337_usergroup')

    objects = User31337Manager()

    class Meta:
        managed = False
        db_table = 'user_31337'

class UserEliteManager(models.Manager):
    def create_user(self, id, password=None, **extra_fields):
        user = self.model(id=id, **extra_fields)
        if password:
            user.password = make_password(password)
        user.save()
        return user

class UserElite(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=125, blank=True, null=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    usermajor = models.CharField(max_length=50, blank=True, null=True)
    usergroup = models.ForeignKey('UserGroupElite', models.DO_NOTHING, db_column='usergroup', blank=True, null=True, related_name='userelite_usergroup')

    objects = UserEliteManager()

    class Meta:
        managed = False
        db_table = 'user_elite'


class UserGroup31337(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group_31337'


class UserGroupElite(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group_elite'
