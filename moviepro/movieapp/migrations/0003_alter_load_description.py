# Generated by Django 4.2 on 2023-05-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_rename_date_load_year_load_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='description',
            field=models.TextField(),
        ),
    ]
