# Generated by Django 3.2.4 on 2022-04-03 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0007_rename_pinenee_terpeneprofile_pinene'),
    ]

    operations = [
        migrations.AddField(
            model_name='terpeneprofile',
            name='humulene',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
