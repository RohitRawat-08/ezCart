# Generated by Django 5.1.1 on 2024-12-28 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Log_In', '0005_remove_myordersmodel_order_id_alter_myordersmodel_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myordersmodel',
            old_name='id',
            new_name='order_id',
        ),
    ]