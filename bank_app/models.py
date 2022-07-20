from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ", " + self.email

    def validate_user(self, user):
        if not user.email:
            return ValueError("Email is required for registration.")
        if not user.first_name:
            return ValueError("First name is required for registration.")
        if not user.last_name:
            return ValueError("Last name is required for registration.")
        if not user.password:
            return ValueError("Password is required for registration.")


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    type = models.CharField(max_length=30)
    date_created = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
