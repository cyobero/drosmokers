from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from strains.forms import StrainForm, BatchForm, TerpeneProfileForm, GrowerForm
from strains.models import Strain, Batch, TerpeneProfile


# Create your views here.
def grower_form(request):
    if request.method == "POST":
        form = GrowerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Grower '{}' successfull added".format(
                form.cleaned_data["grower"]))
        return render(request, "grower_form.html", {"form": form})
    form = GrowerForm
    return render(request, "grower_form.html", {"form": form})


def terpenes_form(request, batch_id):
    batch = Batch.objects.filter(id=int(batch_id))
    if not batch.exists():
        messages.error(request, "No batch found with id = {}".format(batch_id))
    else:
        batch = batch[0]

    if request.method == "POST":
        form = TerpeneProfileForm(request.POST)
        if form.is_valid():
            tp = {
                "id": batch_id,
                "limonene": form.cleaned_data["limonene"],
                "pinene": form.cleaned_data["pinene"],
                "caryophillene": form.cleaned_data["caryophillene"],
                "myrcene": form.cleaned_data["myrcene"],
                "terpinene": form.cleaned_data["terpinene"]
            }

            new_obj = TerpeneProfile(tp)
            new_obj.save()
            messages.success(request, "New terpene profile added!")
        return render(request, "terpenes_form.html", {"form": form, "batch": batch})
    form = TerpeneProfileForm
    return render(request, "terpenes_form.html", {"form": form, "batch": batch})


def batch_form(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Batch successfully added!")
        return render(request, "batch_form.html", {"form": form})
    form = BatchForm()
    return render(request, "batch_form.html", {"form": form})


def batches_view(request):
    batches = Batch.objects.all()
    return render(request, "batches.html", {"batches": batches})


def strain_form(request):
    if request.method == "POST":
        form = StrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Strain successfully added")
        return render(request, "strain_form.html", {"form": form})
    form = StrainForm()
    return render(request, 'strain_form.html', {'form': form})
