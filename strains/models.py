from django.db import models

# Create your models here.


class Strain(models.Model):
    family_choices = (
        ('I', 'Indica'),
        ('S', 'Sativa'),
        ('H', 'Hybrid')
    )
    family = models.CharField(choices=family_choices, max_length=6)
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return str(self.name)


class Grower(models.Model):
    name = models.CharField(max_length=256)
    website = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Batch(models.Model):
    strain = models.ForeignKey(Strain, on_delete=models.CASCADE)
    harvest_date = models.DateField()
    package_date = models.DateField()
    test_date = models.DateField()
    thc_content = models.DecimalField(
        decimal_places=2, max_digits=5, default=0.0)
    cbd_content = models.DecimalField(
        decimal_places=2, max_digits=5, default=0.0)
    grower = models.ForeignKey(Grower, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", default="default_bud.jpeg")

    def __str__(self):
        return "%s by %s (%i)" % (self.strain.name, self.grower.name, self.id)


class TerpeneProfile(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    limonene = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    pinene = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    caryophyllene = models.DecimalField(
        decimal_places=2, max_digits=6, default=0.0)
    myrcene = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    humulene = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    terpinene = models.DecimalField(
        decimal_places=2, max_digits=5, default=0.0)
    linalool = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)

    def get_batch(self):
        obj = Batch.objects.get(id=self.id)
        return obj


class Rating(models.Model):
    score_choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    score = models.IntegerField(choices=score_choices, null=True, blank=False)
