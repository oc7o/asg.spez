from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):

    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address"
    )

    profile_image = models.ImageField(
        _("Users Profile Image"),
        upload_to="profile_images/",
        height_field=None,
        width_field=None,
        max_length=None,
    )

    USERNAME_FIELD = "username"  # e.g: "username", "email"
    EMAIL_FIELD = "email"  # e.g: "email", "primary_email"
