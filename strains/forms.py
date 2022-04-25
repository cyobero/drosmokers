from django.forms import ModelForm, ValidationError
from django.contrib import messages
from strains.models import Strain, TerpeneProfile
from strains.models import Strain, Batch, Grower, Rating
import django.forms as forms


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["batch", "score"]


class StrainForm(ModelForm):
    class Meta:
        family_choices = (
            ('I', 'Indica'),
            ('S', 'Sativa'),
            ('H', 'Hybrid')
        )

        model = Strain
        fields = ['name', 'family', ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'family': forms.Select(choices=family_choices, attrs={'class': 'form-control'})
        }

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
                  "caryophyllene", "myrcene", "terpinene", "humulene", "linalool"]

        widgets = {
            "limonene": forms.NumberInput(attrs={"class": "form-control", "placeholder": model.limonene}),
            "pinene": forms.NumberInput(attrs={"class": "form-control", }),
            "caryophyllene": forms.NumberInput(attrs={"class": "form-control"}),
            "myrcene": forms.NumberInput(attrs={"class": "form-control"}),
            "terpinene": forms.NumberInput(attrs={"class": "form-control"}),
            "humulene": forms.NumberInput(attrs={"class": "form-control"}),
            "linalool": forms.NumberInput(attrs={"class": "form-control"})
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ["strain", "harvest_date", "final_test_date", "package_date",  "thc_content",
                  "cbd_content", "grower", "image"]

        widgets = {
            "strain": forms.Select(attrs={"class": "form-control"}),
            "harvest_date": DateInput(attrs={"class": "form-control"}),
            "final_test_date": DateInput(attrs={"class": "form-control"}),
            "package_date": DateInput(attrs={"class": "form-control"}),
            "thc_content": forms.NumberInput(attrs={"class": "form-control"}),
            "cbd_content": forms.NumberInput(attrs={"class": "form-control"}),
            "grower": forms.Select(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})
        }


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
