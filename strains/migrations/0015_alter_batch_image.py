# Generated by Django 4.0.3 on 2022-04-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0014_alter_batch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='image',
            field=models.ImageField(default='default_bud.jpeg', upload_to='images/'),
        ),
    ]
