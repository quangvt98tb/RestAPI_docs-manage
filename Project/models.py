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
    phone = models.IntegerField()
    live_at = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'User'


class Document(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    is_deleted = models.BooleanField(auto_created=False)
    # user = models.ForeignKey(User, related_name='user_document', on_delete=models.CASCADE)
    id_user = models.IntegerField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'document'
        ordering = ["-created", "-updated"]
