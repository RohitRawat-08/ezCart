# Generated by Django 5.1.1 on 2024-12-28 16:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log_In', '0006_rename_id_myordersmodel_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='myordersmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
