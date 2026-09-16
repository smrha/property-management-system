from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset
from .forms import AssetForm


def assets_edit_view(request, id):
    asset = get_object_or_404(Asset, id=id)
    if request.method == "POST":
        form = AssetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("assets:assets_detail", id=asset.id)

    else:

        form = AssetForm(
            instance=asset
        )
    context = {
            "form": form,
            'asset': asset,
        }
    return render(request, "assets/assets_edit.html", context)

def assets_detail_view(request, id):
    asset = get_object_or_404(Asset, id=id)
    context = {
        'asset': asset,
    }
    return render(request, "assets/assets_detail.html", context)

def assets_create_view(request):

    if request.method == "POST":
        form = AssetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("assets:assets_list")

    else:
        form = AssetForm()

    context = {
        'form': form
    }
    return render(request, "assets/assets_create.html", context)

def assets_list_view(request):
    assets = Asset.objects.all()
    context = {
        'assets': assets,
    }
    return render(request, 'assets/assets_list.html', context)