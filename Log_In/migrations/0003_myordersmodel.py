# Generated by Django 5.1.1 on 2024-12-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log_In', '0002_address_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrdersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=500)),
                ('img_url', models.URLField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
            ],
        ),
    ]
