# Generated by Django 3.2.4 on 2022-04-01 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0005_batch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strain',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
