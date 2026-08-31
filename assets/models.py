from django.db import models

class Location(models.Model):

    class LocationType(models.TextChoices):
        ORGANIZATION = "organization", "سازمان"
        BUILDING = "building", "ساختمان"
        FLOOR = "floor", "طبقه"
        ROOM = "room", "اتاق"
        WAREHOUSE = "warehouse", "انبار"
        OFFICE = "office", "دفتر"
        OTHER = "other", "سایر"

    name = models.CharField(
        max_length=150,
        verbose_name="نام محل"
    )

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="کد محل"
    )

    location_type = models.CharField(
        max_length=20,
        choices=LocationType.choices,
        default=LocationType.OTHER,
        verbose_name="نوع محل"
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="محل والد"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        verbose_name = "محل"
        verbose_name_plural = "محل‌ها"
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class AssetCategory(models.Model):

    name = models.CharField(
        max_length=150,
        verbose_name="نام دسته‌بندی"
    )

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="کد دسته‌بندی"
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="دسته‌بندی والد"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="فعال"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی"
    )

    class Meta:
        verbose_name = "دسته‌بندی دارایی"
        verbose_name_plural = "دسته‌بندی‌های دارایی"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Asset(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "active", "در حال استفاده"
        AVAILABLE = "available", "آماده تخصیص"
        REPAIR = "repair", "در تعمیر"
        DAMAGED = "damaged", "خراب"
        DISPOSED = "disposed", "اسقاط شده"
        LOST = "lost", "مفقود"
        SOLD = "sold", "فروخته شده"

    # -------------------------
    # Identification
    # -------------------------

    asset_code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="کد اموال"
    )

    name = models.CharField(
        max_length=255,
        verbose_name="نام دارایی"
    )

    serial_number = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        verbose_name="شماره سریال"
    )

    # -------------------------
    # Classification
    # -------------------------

    category = models.ForeignKey(
        "AssetCategory",
        on_delete=models.PROTECT,
        related_name="assets",
        verbose_name="دسته‌بندی"
    )

    brand = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="برند"
    )

    model = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="مدل"
    )

    # -------------------------
    # Purchase Information
    # -------------------------

    purchase_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ خرید"
    )

    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="قیمت خرید"
    )

    # -------------------------
    # Location
    # -------------------------

    location = models.ForeignKey(
        "Location",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assets",
        verbose_name="محل استقرار"
    )

    # -------------------------
    # Status
    # -------------------------

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
        verbose_name="وضعیت"
    )

    # -------------------------
    # Warranty
    # -------------------------

    warranty_start = models.DateField(
        null=True,
        blank=True,
        verbose_name="شروع گارانتی"
    )

    warranty_end = models.DateField(
        null=True,
        blank=True,
        verbose_name="پایان گارانتی"
    )

    # -------------------------
    # Media
    # -------------------------

    image = models.ImageField(
        upload_to="assets/",
        null=True,
        blank=True,
        verbose_name="تصویر"
    )

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات"
    )

    # -------------------------
    # System
    # -------------------------

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
            verbose_name = "دارایی"
            verbose_name_plural = "دارایی ها"
            ordering = ["name"]

    def __str__(self):
        return f"{self.asset_code} - {self.name}"