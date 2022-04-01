from django.shortcuts import render
from strains.forms import StrainForm
from strains.models import Strain


# Create your views here.
def strain_form(request):
    if request.method == "POST":
        form = StrainForm(request.POST)
        if form.is_valid():
            _ = form.save()
        return render(request, 'success.html')
    form = StrainForm()
    return render(request, 'strain_form.html', {'form': form})
