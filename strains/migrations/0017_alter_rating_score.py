# Generated by Django 4.0.3 on 2022-04-12 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0016_terpeneprofile_linalool_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
    ]
