from strains.models import Strain, Batch, TerpeneProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from strains.forms import StrainForm, BatchForm, TerpeneProfileForm, GrowerForm, RatingForm


# Create your views here.
def rating_form(request):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rating successfully added!")
            return redirect("success")
        return render(request, "rating_form.html", {"form": form})
    form = RatingForm
    return render(request, "rating_form.html", {"form": form})


def terpenes_view(request, batch_id):
    terp = TerpeneProfile.objects.filter(batch__id=int(batch_id))
    return render(request, "terpene_profile.html", {"terp": terp, "batch_id": int(batch_id)})


def grower_form(request):
    if request.method == "POST":
        form = GrowerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Grower '{}' successfull added".format(
                form.cleaned_data["name"]))
            return redirect('success')
        return render(request, "grower_form.html", {"form": form})
    form = GrowerForm
    return render(request, "grower_form.html", {"form": form})


def terpenes_form(request, batch_id):
    batch = get_object_or_404(Batch, id=int(batch_id))

    if request.method == "POST":
        form = TerpeneProfileForm(request.POST)
        if form.is_valid():
            profile = TerpeneProfile(batch=batch,
                                     limonene=form.cleaned_data["limonene"],
                                     pinene=form.cleaned_data["pinene"],
                                     caryophyllene=form.cleaned_data["caryophyllene"],
                                     myrcene=form.cleaned_data["myrcene"],
                                     humulene=form.cleaned_data["humulene"],
                                     terpinene=form.cleaned_data["terpinene"],
                                     linalool=form.cleaned_data["linalool"])
            profile.save()

            messages.success(request, "New terpene profile added!")
            return redirect("success")
        return render(request, "terpenes_form.html", {"form": form, "batch": batch})
    form = TerpeneProfileForm
    return render(request, "terpenes_form.html", {"form": form, "batch": batch,
                                                  "batch_id": batch_id})


def batch_form(request):
    if request.method == "POST":
        form = BatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New batch successfully added!")
            return redirect("success")
        return render(request, "batch_form.html", {"form": form})
    form = BatchForm()
    return render(request, "batch_form.html", {"form": form})


def batches_view(request):
    batches = Batch.objects.all().order_by('-id')
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
