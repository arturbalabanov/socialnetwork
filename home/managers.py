from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UserProfileManager(BaseUserManager):
    def _create_user(self, username, password, email, gender, is_superuser, is_staff, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError("The email field is required")
        email = self.normalize_email(email)

        user = self.model(username=username,
                          email=email,
                          gender=gender,
                          is_superuser=is_superuser,
                          is_staff=is_staff,
                          is_active=True,
                          last_login=now,
                          date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, username, password, email, gender, **extra_fields):
        return self._create_user(username, password, email, gender, False, False, **extra_fields)

    def create_superuser(self, username, password, email, gender, **extra_fields):
        return self._create_user(username, password, email, gender, True, True, **extra_fields)
