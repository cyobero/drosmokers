# Generated by Django 4.0.3 on 2022-04-25 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0019_rename_final_test_date_batch_test_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='test_date',
            new_name='final_test_date',
        ),
    ]
