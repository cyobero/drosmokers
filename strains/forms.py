from django.forms import ModelForm, ValidationError
from django.contrib import messages
from strains.models import Strain


class StrainForm(ModelForm):
    class Meta:
        model = Strain
        fields = ['name', 'family', ]

    def clean_name(self):
        name = self.cleaned_data["name"].lower()
        if Strain.objects.filter(name=name).exists():
            raise ValidationError(('The strain %(name)s has already been added.'),
                                  params={'name': name.title()}
                                  )
        return name
