from django.contrib.auth.models import AbstractUser
from django.db import models

from organization.models import Department, Position

class User(AbstractUser):

    class Gender(models.TextChoices):
        MALE = "male", "مرد"
        FEMALE = "female", "زن"

    phone = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="شماره موبایل"
    )

    national_code = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        verbose_name="کد ملی"
    )

    first_name = models.CharField(
        max_length=100,
        verbose_name="نام"
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="نام خانوادگی"
    )

    personnel_code = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name="کد پرسنلی"
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender,
        null=True,
        blank=True
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
        verbose_name="واحد سازمانی"
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
        verbose_name="سمت سازمانی"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
