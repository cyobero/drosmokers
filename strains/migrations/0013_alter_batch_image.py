# Generated by Django 4.0.3 on 2022-04-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0012_alter_batch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='image',
            field=models.ImageField(blank=True, default='default_bud.jpeg', null=True, upload_to='images'),
        ),
    ]
