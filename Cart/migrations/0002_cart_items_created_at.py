# Generated by Django 5.1.1 on 2024-12-28 17:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_items',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]