# Generated by Django 4.2.3 on 2023-08-24 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_product_product_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
