# Generated by Django 4.0.3 on 2022-03-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0003_terpeneprofile_terpinene'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grower',
            name='website',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
