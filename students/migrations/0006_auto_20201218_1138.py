# Generated by Django 3.1.2 on 2020-12-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_students_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='about',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]