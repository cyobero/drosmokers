from django.forms import ModelForm
from strains.models import Strain


class StrainForm(ModelForm):
    class Meta:
        model = Strain
        fields = ['name', 'family', ]
