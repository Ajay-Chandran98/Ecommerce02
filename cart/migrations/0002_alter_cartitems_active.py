# Generated by Django 4.2.6 on 2023-11-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
