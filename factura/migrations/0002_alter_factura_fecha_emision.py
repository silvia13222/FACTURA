# Generated by Django 3.2.3 on 2021-06-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='fecha_emision',
            field=models.DateField(max_length=100),
        ),
    ]
