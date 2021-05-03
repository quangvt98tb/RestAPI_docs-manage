from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # Delete not use field
    username = None
    last_login = None
    is_staff = None
    is_superuser = None

    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12)
    role_id = models.IntegerField()  # 1: user ; 0: admin ; 2: block
    live_at = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'User'


class UserShare(models.Model):
    id_usershare = models.IntegerField()
    id_doc = models.IntegerField()
    id_role = models.IntegerField()  # role: {1: fix, 2: read }
    note = models.TextField()

    class Meta:
        db_table = 'usershare'


class Comment(models.Model):
    id_user = models.IntegerField()
    id_doc = models.IntegerField()
    comment = models.TextField()

    class Meta:
        db_table = 'comment'


class RoleShare(models.Model):
    # 1: user; 0: admin
    name_role = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'roleshare'


class RoleUser(models.Model):
    name_role = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'roleuser'


class Category(models.Model):
    name_category = models.CharField(max_length=100)
    note = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'


class Document(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    category_id = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    id_author = models.IntegerField()
    update_last_by = models.IntegerField()
    updated = models.DateField(auto_now=True, auto_now_add=False)
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'document'
