# Generated by Django 3.2.3 on 2021-07-06 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.JSONField(default=[]),
        ),
    ]
