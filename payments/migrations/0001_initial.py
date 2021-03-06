# Generated by Django 4.0 on 2022-01-22 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPayment', models.DecimalField(decimal_places=3, max_digits=10)),
                ('paymentType', models.CharField(choices=[('TARJETA', 'tarjeta'), ('EFECTIVO', 'efectivo')], max_length=255)),
                ('statusPayment', models.CharField(choices=[('PENDIENTE', 'pendiente'), ('PAGADO', 'pagado')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table')),
            ],
        ),
    ]
