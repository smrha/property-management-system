from django.db import models
from django.conf import settings

class Department(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name="نام واحد"
    )

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="کد واحد"
    )

    parent = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="واحد بالادستی"
    )

    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_departments",
        verbose_name="مدیر واحد"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Position(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان سمت"
    )

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="کد سمت"
    )

    level = models.PositiveIntegerField(
        default=1,
        verbose_name="سطح سازمانی"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title