from django.forms import ModelForm, ValidationError
from django.contrib import messages
from strains.models import Strain, TerpeneProfile
from strains.models import Strain, Batch, Grower


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


class TerpeneProfileForm(ModelForm):
    class Meta:
        model = TerpeneProfile
        fields = ["limonene", "pinene",
                  "caryophillene", "myrcene", "terpinene"]


class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ["strain", "harvest_date", "package_date", "test_date", "thc_content",
                  "cbd_content", "terpenes", "grower", "image"]


class GrowerForm(ModelForm):
    class Meta:
        model = Grower
        fields = ["name", "website"]

    def clean_name(self):
        name = self.cleaned_data["name"].lower()
        if Grower.objects.filter(name__iexact=name).exists():
            raise ValidationError(
                ("A grower with a similar name has already been added."))
        return name
