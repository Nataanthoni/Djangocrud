# Generated by Django 3.1.2 on 2020-12-16 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schools',
            old_name='disctrict',
            new_name='district',
        ),
    ]