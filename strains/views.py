from django.shortcuts import render, redirect
from django.contrib import messages
from strains.forms import StrainForm
from strains.models import Strain


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
