from django.db import models

# Create your models here.


class Strain(models.Model):
    family = (('I', 'Indica', 'S', 'Sativa', 'H', 'Hybrid'))
    name = models.CharField(max_length=256)


class Batch(models.Model):
    strain = models.ForeignKey(Strain, on_delete=models.CASCADE)
    harvest_date = models.DateField()
    package_date = models.DateField()
    test_date = models.DateField()
    thc_content = models.DecimalField(decimal_places=2, max_digits=5)
    cbd_content = models.DecimalField(decimal_places=2, max_digits=5)


class Terpene(models.Model):
    name = models.CharField(max_length=128)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    batch = models.ManyToManyField(Batch)
