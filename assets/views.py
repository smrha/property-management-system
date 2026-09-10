from django.shortcuts import render, redirect
from .models import Asset
from .forms import AssetForm

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