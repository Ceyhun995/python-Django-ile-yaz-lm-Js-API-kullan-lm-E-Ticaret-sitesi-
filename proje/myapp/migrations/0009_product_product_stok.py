# Generated by Django 4.2.3 on 2023-08-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_navcover'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_stok',
            field=models.PositiveIntegerField(default=1, verbose_name='stok'),
        ),
    ]
