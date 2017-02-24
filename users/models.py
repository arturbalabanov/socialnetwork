import arrow
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote

from home.managers import UserProfileManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', "Male"),
        ('F', "Female"),
    )

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    birth_date = models.DateField(blank=True, null=True)
    friends = models.ManyToManyField('self')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [email, gender]

    objects = UserProfileManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @property
    def age(self):
        today = arrow.utcnow().date()
        delta = arrow.arrow.relativedelta(today, self.birth_date)
        return delta.years

    @property
    def friends_count(self):
        return self.friends.count()

    def get_absolute_url(self):
        return '/users/profile/%s/' % urlquote(self.username)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
