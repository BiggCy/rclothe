# Generated by Django 3.2.3 on 2021-07-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210704_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='multi_images',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.FileField(default='', upload_to='shop/images'),
        ),
    ]
