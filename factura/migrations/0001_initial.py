# Generated by Django 3.2.3 on 2021-06-09 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=100, unique=True)),
                ('cliente_nombre', models.CharField(max_length=100, unique=True)),
                ('cliente_direccion', models.CharField(blank=True, max_length=100)),
                ('fecha_emision', models.DateField(default=2021, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LineaFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=5, max_length=100)),
                ('unidades', models.PositiveIntegerField(default=1)),
                ('factura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='factura.factura')),
            ],
        ),
    ]
