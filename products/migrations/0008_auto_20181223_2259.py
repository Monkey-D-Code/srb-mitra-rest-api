# Generated by Django 2.1.4 on 2018-12-23 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181223_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='unit',
            new_name='sold_unit',
        ),
    ]
