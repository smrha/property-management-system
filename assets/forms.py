from django import forms
from accounts.models import User
from .models import Asset, Location, AssetAssignment


class AssetForm(forms.ModelForm):
    name = forms.CharField(
        label="نام دارایی",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "نام دارایی",
            }
        ),
    )
    asset_code = forms.CharField(
        label="کد اموال",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "کد اموال",
            }
        ),
    )
    serial_number = forms.CharField(
        label="شماره سریال",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "شماره سریال",
            }
        ),
    )
    category = forms.ChoiceField(
        choices=Asset.Status.choices,
        label="دسته‌بندی",
        widget=forms.Select(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "دسته‌بندی",
            }
        ),
    )
    brand = forms.CharField(
        label="برند",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "برند",
            }
        ),
    )
    model = forms.CharField(
        label="مدل",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "مدل",
            }
        ),
    )
    purchase_date = forms.DateField(
        label="تاریخ خرید",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "تاریخ خرید",
            }
        ),
    )
    purchase_price = forms.DecimalField(
        label="قیمت خرید",
        widget=forms.NumberInput(
            attrs={
                "type": "number",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "قیمت خرید",
                "min": "0",
            }
        ),
    )
    location = forms.CharField(
        label="محل استقرار",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "محل استقرار",
            }
        ),
    )
    status = forms.CharField(
        label="وضعیت",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "وضعیت",
            }
        ),
    )
    warranty_start = forms.DateField(
        label="شروع گارانتی",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "شروع گارانتی",
            }
        ),
    )
    warranty_end = forms.DateField(
        label="پایان گارانتی",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "پایان گارانتی",
            }
        ),
    )
    image = forms.CharField(
        label="تصویر",
        widget=forms.ClearableFileInput(
            attrs={
                "class": "cursor-pointer bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand block w-full shadow-xs placeholder:text-body",
                "placeholder": "تصویر",
            }
        ),
    )
    description = forms.CharField(
        label="توضیحات",
        widget=forms.Textarea(
            attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "placeholder": "توضیحات",
            }
        ),
    )
    is_active = forms.BooleanField(
        label="فعال",
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-4 h-4 text-neutral-blue border-default-medium bg-neutral-secondary-medium rounded-full checked:border-brand focus:ring-2 focus:outline-none focus:ring-brand-subtle border border-default appearance-none",
                "placeholder": "فعال",
            }
        ),
    )

    class Meta:
        model = Asset

        fields = [
            "asset_code",
            "name",
            "serial_number",
            "category",
            "brand",
            "model",
            "purchase_date",
            "purchase_price",
            "location",
            "status",
            "warranty_start",
            "warranty_end",
            "image",
            "description",
            "is_active",
        ]

class AssetAssignmentForm(forms.ModelForm):
    
    
    class Meta:
        model = AssetAssignment

        fields = [
            'employee',
            'description'
        ]

        widgets = {
            "employee": forms.Select(attrs={
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            }),
            "description": forms.Textarea(attrs={
                "class": "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
                "rows": 4,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["employee"].queryset = User.objects.filter(
            is_active=True
        ).order_by("first_name", "last_name")
