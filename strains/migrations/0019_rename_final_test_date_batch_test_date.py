# Generated by Django 4.0.3 on 2022-04-25 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strains', '0018_rename_test_date_batch_final_test_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='final_test_date',
            new_name='test_date',
        ),
    ]