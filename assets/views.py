from django.shortcuts import render
from .models import Asset


def assets_list_view(request):
    assets = Asset.objects.all()
    context = {
        'assets': assets,
    }
    return render(request, 'assets/assets_list.html', context)