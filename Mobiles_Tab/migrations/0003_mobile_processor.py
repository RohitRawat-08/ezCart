# Generated by Django 5.1.1 on 2024-12-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mobiles_Tab', '0002_alter_mobile_rating_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='processor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Processor'),
        ),
    ]