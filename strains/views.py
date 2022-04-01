from django.shortcuts import render
from django.contrib import messages
from strains.forms import StrainForm
from strains.models import Strain, Batch


# Create your views here.


def strain_form(request):
    if request.method == "POST":
        form = StrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Strain successfully added")
        return render(request, "strain_form.html", {"form": form})
    form = StrainForm()
    return render(request, 'strain_form.html', {'form': form})


def batches_view(request):
    batches = Batch.objects.all()
    return render(request, "batches.html", {"batches": batches})
